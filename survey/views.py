import json
from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import (
    Count,
)

from .models      import (
        Survey,
        UserSurvey,
        EffectiveDate,
        EvasionGrade,
        Result,
)
from user.models  import (
        User
)
from user.utils  import Login_decorator

import my_settings

def make_survey_result(user_id):
    user = User.objects.get(id = user_id)
        
    FKE = 'finance_knowledge_evaluation'
    REE = 'risk_evasion_evaluation'
    LEE = 'loss_evasion_evaluation'

    result = {
            'user_info': {
                'email': user.email,                
                },
            FKE:3,
            REE:7,
            LEE:7,
            'evasion_grade':{}
    }

    evasion_grade = {}
    for evasion in EvasionGrade.objects.all().order_by('-grade'):
        evasion_grade[evasion.grade] = evasion.tendency
    result['evasion_grade'] = evasion_grade

    user_surveys = UserSurvey.objects.select_related('survey').filter(user_id = user_id)
    FKEs = list(user_surveys.filter(survey__category_id = 1).order_by('survey_id'))
    
    # 금융지식 평가
    if FKEs[0].answer != 'A':
        result[FKE] -= 1
    if FKEs[1].answer != 'A':
        result[FKE] -= 1
    if FKEs[2].answer != 'A':
        result[FKE] -= 1

    # 위험 회피 평가
    REEs = list(user_surveys.filter(survey__category_id = 2).order_by('survey_id'))
    
    if REEs[0].answer == 'B':
        result[REE] -= 2
    if REEs[1].answer == 'B':
        result[REE] -= 1
    if REEs[2].answer == 'B':
        result[REE] -= 1
    if REEs[3].answer == 'B':
        result[REE] -= 1
    if REEs[4].answer == 'B':
        result[REE] -= 1
    
    # 손실 회피 평가
    LEEs = list(user_surveys.filter(survey__category_id = 3).order_by('survey_id'))
    
    if LEEs[0].answer == 'B':
        result[LEE] -= 1
    if LEEs[1].answer == 'B':
        result[LEE] -= 1
    if LEEs[2].answer == 'B':
        result[LEE] -= 2
    if LEEs[3].answer == 'B':
        result[LEE] -= 1
    if LEEs[4].answer == 'B':
        result[LEE] -= 1

    updated, created = Result.objects.update_or_create(
            user_id=user_id, 
            effective_date_id=user_surveys.last().survey.effective_date_id,  
            defaults={
                'data':json.dumps(result)
                }
            )
    
    if updated or created:
        user_surveys.all().delete()

    return result
    

def generate_response_for_survey(user_id):
    response     = {
            "survey":{
                "id"     : 0, 
                "content": {},
                }, 
            "progress":{
                "current": 1,
                "total"  : my_settings.SURVEYS_COUNT 
                }
            }

    user_surveys = UserSurvey.objects.select_related('user', 'survey').filter(user_id = user_id)
    count        = user_surveys.count()     

    if not count:        
        user_surveys.delete()
        survey = Survey.objects.first()
        
        response['survey']['id']        = survey.id
        response['survey']['content']   = survey.content

        # parsing 해서 주는 방법
        # question, *answers = survey.content.split('|')
        # content = {
        #     'question':'',
        #     'examples':[]
        #     }

        # for answer in *answers:
        #     data         = {}
        #     arr = answer.split(')')
        #     data.id      = arr[0][-1:0].upper()
        #     data.example = arr[1]
        #     content['examples'].append(data)

        # response['survey']['content'] = json.dumps(content)
        return response
        

    if count < my_settings.SURVEYS_COUNT:
        # 설문 계속 진행
        next_survey = Survey.objects.get(id = count + 1)
        
        response['survey']['id']        = next_survey.id
        response['survey']['content']   = next_survey.content
        response['progress']['current'] = UserSurvey.objects.filter(user_id=user_id).count() + 1

        return response        
            
    # 설문조사 결과 리턴
    return make_survey_result(user_id)


class StartView(View):
    @Login_decorator 
    def get(self, request):
        try:
            user_id = User.objects.get(email=request.user['email']).id
            message = generate_response_for_survey(user_id)

            return JsonResponse(message, status=200)

        except Survey.DoesNotExist:
            return JsonResponse({"message":"DATA_NOT_EXIST"}, status=200)


class ResponseView(View):
    @transaction.atomic
    @Login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email = request.user['email'])

            if UserSurvey.objects.filter(user_id = user.id).count() >= my_settings.SURVEYS_COUNT:
                return JsonResponse({"message":"ALREADY_DONE"}, status=201)

            UserSurvey.objects.update_or_create(
                            user_id     = user.id, 
                            survey_id   = data['survey_id'], 
                            defaults = {
                                'answer': data['answer'],
                                'time': data['time'],
                            }
            )

            message = generate_response_for_survey(user.id)

            return JsonResponse(message, status=201)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)


class ResultView(View):
    @Login_decorator
    def get(self, request):
        user_id = User.objects.get(email=request.user['email']).id
        
        result = Result.objects.get(user_id = user_id)
        result = json.loads(result.data)

        evasion_grade = {}
        for evasion in EvasionGrade.objects.all().order_by('grade'):
            evasion_grade[evasion.grade] = evasion.tendency.replace('{0}', '')
        result['evasion_grade'] = evasion_grade
        
        return JsonResponse(result, status=200)

