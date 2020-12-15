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


class SurveyStartView(View):
    @Login_decorator 
    def get(self, request):
        try:
            survey = Survey.objects.first()
        
            return JsonResponse({"message":"SUCCESS", "survey":{"id":survey.id, "content":survey.content}}, status=200)
        except survey.DoesNotExist:
            return JsonResponse({"message":"DATA_NOT_EXIST"}, status=200)

class SurveyResponseView(View):
    def __init__(self):
        self.MAXIMUM_SURVEYS = 3
    
    @transaction.atomic
    @Login_decorator
    def post(self, request):
        data = json.loads(request.body)

        survey_id   = data['survey_id']
        answer      = data['answer']
        time        = data['time']

        user = User.objects.get(email=request.user['email'])
        UserSurvey.objects.update_or_create(user_id = user.id, survey_id = survey_id, defaults={'answer':answer, 'time':time})

        result = self.generate_response_for_survey(user.id, survey_id, answer)

        return JsonResponse({"message":"SUCCESS", "survey":result}, status=201)

    def generate_response_for_survey(self, user_id, survey_id, answer):
        '''
        응답한 설문조사 및 결과에 따라 다음 Survey 대상을 search, 
        해당 Survey ID를 리턴하는 business model 구현.

        만약 모든 설문이 끝나면 Survey ID 대신 '설문조사 결과'를 return.
        '''
        survey = None
        if UserSurvey.objects.filter(user_id=user_id).exclude(answer='').count() < self.MAXIMUM_SURVEYS:
            next_survey = Survey.objects.get(id = survey_id + 1)
            survey = {
                        'id'     : next_survey.id,
                        'content': next_survey.content,
                    }
        else:
            items = list(UserSurvey.objects.values('answer').annotate(count=Count('id')))
            item = max(items, key=lambda x : x['count'])
                                    
            if item['answer'] == 'A':
                survey= {
                            'id'     : 0,
                            'content': InvestType.objects.get(id=1).content
                        }
            else:
                survey = {
                            'id'     : 0,
                            'content': InvestType.objects.get(id=2).content
                        }

        return survey
