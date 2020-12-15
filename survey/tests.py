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
)

class SurveyTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        country = Country.objects.create(name_kor='대한민국', name_eng='republic of korea')

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

        Survey.objects.create(id=1, content='survey1')
        Survey.objects.create(id=2, content='survey2')
        Survey.objects.create(id=3, content='survey3')

        InvestType.objects.create(id=1, content='your type is A')
        InvestType.objects.create(id=2, content='your type is B')

    def tearDown(self):
        InvestType.objects.all().delete()
        UserSurvey.objects.all().delete()
        Survey.objects.all().delete()
        User.objects.all().delete()
        Country.objects.all().delete()

    def test_survey_get_start_success(self):
        response = self.client.get('/survey/start', **self.headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'SUCCESS')
        self.assertEqual(response.json()['survey']['content'], 'survey1')
        
    def test_survey_get_start_not_exist(self):
        response = self.client.get('/survey/start', **self.headers)

        self.assertNotEqual(response.json(), {"message", "DATA_NOT_EXIST"})
    
    def test_survey_post_response_and_return_next_survey_success(self):
        response = self.client.post(
                        '/survey/input',
                        {'survey_id':1, 'answer':'A', 'time':5},
                        content_type='application/json',
                        **self.headers,
                    )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['survey']['content'], 'survey2')

    def test_survey_post_response_and_return_result_success(self):
        UserSurvey.objects.create(user_id=1, survey_id=1, answer='A', time=5)
        UserSurvey.objects.create(user_id=1, survey_id=1, answer='B', time=10)
        response = self.client.post(
                        '/survey/input',
                        {'survey_id':3, 'answer':'A', 'time':12},
                        content_type='application/json',
                        **self.headers,
                    )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['survey']['content'], 'your type is A')
