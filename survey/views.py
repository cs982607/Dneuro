import json
from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import (
    Count,
    Max,
    F,
)

from .models      import (
        Survey,
        UserSurvey,
        InvestType,
)
from user.models  import (
        User
)
from user.utils  import Login_decorator

import my_settings


def generate_response_for_survey(user_id):
    survey = None
    count = UserSurvey.objects.filter(user_id=user_id).count() 
    if count < my_settings.SURVEYS_COUNT:
        next_survey = Survey.objects.get(id = count + 1)
        survey = {
                'survey':{
                    'id'     : next_survey.id,
                    'content': next_survey.content,
                    },
                "progress":{
                    "current": UserSurvey.objects.filter(user_id=user_id).count() + 1,
                    "total"  : my_settings.SURVEYS_COUNT 
                    }
                }

    else:
        items = list(UserSurvey.objects.values('answer').annotate(count=Count('id')))
        item = max(items, key=lambda x : x['count'])
                                
        if item['answer'] == 'A':
            survey= {
                        'result': InvestType.objects.get(id=1).content
                    }
        else:
            survey = {
                        'result': InvestType.objects.get(id=2).content
                    }

    return survey


class SurveyStartView(View):
    @Login_decorator 
    def get(self, request):
        try:
            message = {
                        "message":"SUCCESS", 
                        "survey":{
                            "id"     : 0, 
                            "content": ''
                            }, 
                        "progress":{
                            "current": 1,
                            "total"  : my_settings.SURVEYS_COUNT 
                        }
                    }

            user_serveys = UserSurvey.objects.select_related('user', 'survey')
            surveys      = user_serveys.filter(user__email = request.user['email'])

            if not surveys.count() or surveys.count() == my_settings.SURVEYS_COUNT:
                # user의 설문 정보가 없거나 이미 완료한 상태이면 처음부터 시작
                surveys.delete()
                survey = Survey.objects.first()
                
                message['survey']['id']      = survey.id
                message['survey']['content'] = survey.content

            else:
                # user의 설문 정보가 중간밖에 없다면
                survey = generate_response_for_survey(User.objects.get(email=request.user['email']).id)
                message['survey']['id']        = survey['survey']['id']
                message['survey']['content']   = survey['survey']['content']
                message['progress']['current'] = surveys.count() + 1

            return JsonResponse(message, status=200)

        except Survey.DoesNotExist:
            return JsonResponse({"message":"DATA_NOT_EXIST"}, status=200)

class SurveyResponseView(View):
    @transaction.atomic
    @Login_decorator
    def post(self, request):
        try:
            user = User.objects.get(email = request.user['email'])

            if UserSurvey.objects.filter(user_id = user.id).count() >= my_settings.SURVEYS_COUNT:
                return JsonResponse({"message":"ALREADY_DONE"}, status=201)
            
            data = json.loads(request.body)

            survey_id   = data['survey_id']
            answer      = data['answer']
            time        = data['time']
            user        = User.objects.get(email=request.user['email'])
            
            UserSurvey.objects.update_or_create(survey_id=survey_id, user_id=user.id,
                                                defaults={
                                                    'answer':answer,
                                                    'time':time
                                                    })
            '''
            UserSurvey.objects.create(
                            user_id     = user.id, 
                            survey_id   = survey_id, 
                            answer      = answer,
                            time        = time,
            )
            '''

            result = generate_response_for_survey(user.id)

            return JsonResponse({"message":"SUCCESS", "survey":result}, status=201)
        except:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)


