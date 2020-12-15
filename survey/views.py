import json
from django.views   import View
from django.http    import JsonResponse

from .models      import (
        Survey,
        UserSurvey,
)

class SurveyResponseView(View):
    def post(self, request):
        data = json.loads(request.body)

       #user_id     = request.user
        survey_id   = data['survey_id']
        answer      = data['answer']

        next_survey_id = GenerateSurveyToSend(survey_id, answer)

        survey = Survey.objects.get(id = next_survey_id)
        
        result = survey.content
        return JsonResponse({"message":"SUCCESS", "data":result}, status=201)

    def GenerateSurveyToSend(self, survey_id, answer):
        '''TO DO
        응답한 설문조사 및 결과에 따라 다음 Survey 대상을 search, 
        해당 Survey ID를 리턴하는 business model 구현.

        만약 모든 설문이 끝나면 Survey ID 대신 '설문조사 결과'를 return.
        '''
        pass






