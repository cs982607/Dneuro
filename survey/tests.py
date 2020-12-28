import bcrypt
from datetime import datetime

from django.test import TestCase, Client

from user.models import (
        User,
        Country,
)
from .models     import (
        Survey,
        UserSurvey,
        InvestType,
        Category,
        EffectiveDate,
        Result,
)

import my_settings


class SurveyTest(TestCase):
    def setUp(self):
        self.client = Client()

        EffectiveDate.objects.create(
            id=1, 
            start_at = datetime(2020, 12, 1), 
            end_at = datetime(2020, 12, 31)
        )

        country = Country.objects.create(name_kor='대한민국', name_eng='KOREA')

        User.objects.create(
                id=1,
                email = 'mock@example.com',
                password = (bcrypt.hashpw('Mockpw1!'.encode('utf-8'), bcrypt.gensalt())).decode(),
                birthday = datetime(1990, 10, 5),
                sex = '남자',
                country_id = country.id
        )

        token = self.client.post(
                    '/user/signin',
                    {'email':'mock@example.com', 'password':'Mockpw1!'},
                    content_type = 'application/json'
                ).json()['token']

        self.headers = {'HTTP_Authorization':token}

        Category.objects.create(id=1, name='금융지식평가')
        Category.objects.create(id=2, name='위험회피평가')
        Category.objects.create(id=3, name='손실회피평가')

        Survey.objects.create(id=1, content='FKE_1', category_id=1, effective_date_id=1)
        Survey.objects.create(id=2, content='FKE_2', category_id=1, effective_date_id=1)
        Survey.objects.create(id=3, content='FKE_3', category_id=1, effective_date_id=1)
        Survey.objects.create(id=4, content='REE_1', category_id=2, effective_date_id=1)
        Survey.objects.create(id=5, content='REE_2', category_id=2, effective_date_id=1)
        Survey.objects.create(id=6, content='REE_3', category_id=2, effective_date_id=1)
        Survey.objects.create(id=7, content='REE_4', category_id=2, effective_date_id=1)
        Survey.objects.create(id=8, content='REE_5', category_id=2, effective_date_id=1)
        Survey.objects.create(id=9, content='LEE_1', category_id=3, effective_date_id=1)
        Survey.objects.create(id=10, content='LEE_2', category_id=3, effective_date_id=1)
        Survey.objects.create(id=11, content='LEE_3', category_id=3, effective_date_id=1)
        Survey.objects.create(id=12, content='LEE_4', category_id=3, effective_date_id=1)
        Survey.objects.create(id=13, content='LEE_5', category_id=3, effective_date_id=1)

    def tearDown(self):
        Result.objects.all().delete()
        UserSurvey.objects.all().delete()
        Survey.objects.all().delete()
        User.objects.all().delete()
        Country.objects.all().delete()
        EffectiveDate.objects.all().delete()
        
    def test_survey_get_start_success(self):
        response = self.client.get('/survey/start', **self.headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['survey']['content'], 'FKE_1')
        
    def test_survey_get_start_not_exist(self):
        response = self.client.get('/survey/start', **self.headers)

        self.assertNotEqual(response.json(), {"message", "DATA_NOT_EXIST"})

    def test_survey_get_start_middle_success(self):
        UserSurvey.objects.create(user_id=1, survey_id=1, time=25, answer='A')
        UserSurvey.objects.create(user_id=1, survey_id=2, time=15, answer='A')
        UserSurvey.objects.create(user_id=1, survey_id=3, time=30, answer='A')
 
        response = self.client.get('/survey/start', **self.headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['survey']['content'], 'REE_1')
        self.assertEqual(response.json()['progress']['current'], 4)
        self.assertEqual(response.json()['progress']['total'], my_settings.SURVEYS_COUNT)
    
    def test_survey_post_response_and_return_next_survey_success(self):
        response = self.client.post(
                        '/survey/input',
                        {'survey_id':1, 'answer':'A', 'time':5},
                        content_type='application/json',
                        **self.headers,
                    )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['survey']['content'], 'FKE_2')
        
    def test_survey_post_response_and_return_result_success(self):
        arr = []
        arr.append(UserSurvey(user_id=1, survey_id=1, answer='A', time=5))
        arr.append(UserSurvey(user_id=1, survey_id=2, answer='A', time=10))
        arr.append(UserSurvey(user_id=1, survey_id=3, answer='B', time=5))
        arr.append(UserSurvey(user_id=1, survey_id=4, answer='A', time=15))
        arr.append(UserSurvey(user_id=1, survey_id=5, answer='B', time=5))
        arr.append(UserSurvey(user_id=1, survey_id=6, answer='A', time=7))
        arr.append(UserSurvey(user_id=1, survey_id=7, answer='B', time=12))
        arr.append(UserSurvey(user_id=1, survey_id=8, answer='A', time=5))
        arr.append(UserSurvey(user_id=1, survey_id=9, answer='B', time=9))
        arr.append(UserSurvey(user_id=1, survey_id=10, answer='B', time=7))
        arr.append(UserSurvey(user_id=1, survey_id=11, answer='B', time=11))
        arr.append(UserSurvey(user_id=1, survey_id=12, answer='A', time=9))

        UserSurvey.objects.bulk_create(arr)

        response = self.client.post(
                        '/survey/input',
                        {'survey_id':13, 'answer':'B', 'time':12},
                        content_type='application/json',
                        **self.headers,
                    )

        self.assertEqual(response.status_code, 201)
        result = response.json()

        self.assertEqual(result['user_info']['email'], 'mock@example.com')
        self.assertEqual(result['finance_knowledge_evaluation'], 2)
        self.assertEqual(result['risk_evasion_evaluation'], 5)
        self.assertEqual(result['loss_evasion_evaluation'], 2)
