import json, jwt, re

import bcrypt
from django.test import (
    TestCase,
    Client
    )
from django.http import JsonResponse

from my_settings import (
    SECRET,
    JWT_ALGORITHM
    )

from .models     import (
    User,
    Country
    )
from .utils      import Login_decorator


class SignUpTestCase(TestCase):
    def setUp(self):
        self.URL    = '/user/signup'
        self.client = Client()

        self.EMAIL    = 'gustjr@gmail.com'
        self.PASSWORD = 'gustjr12'
        self.SEX      = 'man'
        self.BIRTHDAY = '2020-04-30'
        self.COUNTRY  = '대한민국'

        self.country = Country.objects.create(
            id       = 1,
            name_kor = self.COUNTRY,
            name_eng = 'KOREA'

        )

        self.user = User.objects.create(
            email      = self.EMAIL,
            password   = self.PASSWORD,
            sex        = self.SEX,
            birthday   = self.BIRTHDAY,
            country_id = self.country.id
        )

    def tearsDown(self):
        pass

    def test_signup_success(self):

        request = {
            'email'      : 'gustjr1234@gmail.com',
            'password'   : self.PASSWORD,
            'sex'        : self.SEX,
            'birthday'   : self.BIRTHDAY,
            'country'    : self.COUNTRY
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'SUCCESS'})
        self.assertEquals(response.status_code, 200)

    def test_signup_invalid_email(self):

        request = {
            'email'      : 'gustjr',
            'password'   : self.PASSWORD,
            'sex'        : self.SEX,
            'birthday'   : self.BIRTHDAY,
            'country'    : self.COUNTRY
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'INVALID_EMAIL'})
        self.assertEquals(response.status_code, 400)

    def test_signup_invalid_password(self):

        request = {
            'email'      : self.EMAIL,
            'password'   : '1',
            'sex'        : self.SEX,
            'birthday'   : self.BIRTHDAY,
            'country'    : self.COUNTRY
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'INVALID_PASSWORD'})
        self.assertEquals(response.status_code, 400)

    def test_signup_already_email(self):

        request = {
            'email'      : self.EMAIL,
            'password'   : self.PASSWORD,
            'sex'        : self.SEX,
            'birthday'   : self.BIRTHDAY,
            'country'    : self.COUNTRY
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'ALREADY_EMAIL'})
        self.assertEquals(response.status_code, 400)

    def test_signup_key_error(self):

        request = {
            'password'   : self.PASSWORD,
            'sex'        : self.SEX,
            'birthday'   : self.BIRTHDAY,
            'country_id' : self.country.id
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'KEY_ERROR'})
        self.assertEquals(response.status_code, 400)


class SignInTestCase(TestCase):
    def setUp(self):
        self.URL    = '/user/signin'
        self.client = Client()

        self.EMAIL    = 'gustjr@gmail.com'
        self.PASSWORD = bcrypt.hashpw('gustjr12'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.SEX      = 'man'
        self.BIRTHDAY = '2020-04-30'
        self.COUNTRY  = '대한민국'

        self.country = Country.objects.create(
            id       = 1,
            name_kor = self.COUNTRY,
            name_eng = 'KOREA'

        )

        self.user = User.objects.create(
            email      = self.EMAIL,
            password   = self.PASSWORD,
            sex        = self.SEX,
            birthday   = self.BIRTHDAY,
            country_id = 1
        )
        user = User.objects.get(id=self.user.id)
        self.token = jwt.encode({'email':self.user.email}, SECRET, algorithm= JWT_ALGORITHM).decode('utf-8')


    def tearsDown(self):
        pass

    def test_signin_success(self):

        request = {
            'email'      : self.EMAIL,
            'password'   : 'gustjr12'
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'token':self.token})
        self.assertEquals(response.status_code, 200)

    def test_signin_invalid_password(self):

        request = {
            'email'      : self.EMAIL,
            'password'   : '1234'
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'INVALID_PASSWORD'})
        self.assertEquals(response.status_code, 400)

    def test_signin_key_error(self):

        request = {
            'email'      : self.EMAIL,
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'KEY_ERROR'})
        self.assertEquals(response.status_code, 400)

    def test_signin_user_does_not_exist(self):

        request = {
            'email'      : 'aaaaaaa',
            'password'   : self.PASSWORD,
        }

        response = self.client.post(self.URL, request, content_type='application/json')
        self.assertEqual(response.json(),{'message':'USER_DOES_NOT_EXIST'})
        self.assertEquals(response.status_code, 400)

class LoginDecoratorTestCase(TestCase):
    def setUp(self):
        self.URL    = '/user/test'
        self.client = Client()

        self.EMAIL    = 'gustjr@gmail.com'
        self.PASSWORD = 'gustjr12'
        self.SEX      = 'man'
        self.BIRTHDAY = '2020-04-30'
        self.COUNTRY  = '대한민국'

        self.country = Country.objects.create(
            id       = 1,
            name_kor = self.COUNTRY,
            name_eng = 'KOREA'
        )

        self.user = User.objects.create(
            id         = 1,
            email      = self.EMAIL,
            password   = self.PASSWORD,
            sex        = self.SEX,
            birthday   = self.BIRTHDAY,
            country_id = 1
        )
        self.unknown_id = {'email' : 12343434}
        self.invalid_id = {'i'  : self.user.id}
        self.token = jwt.encode({'email':self.user.email}, SECRET, algorithm= JWT_ALGORITHM).decode('utf-8')
        self.unknown_token = jwt.encode(self.unknown_id, SECRET, algorithm= JWT_ALGORITHM).decode('utf-8')
        self.invalid_token = jwt.encode(self.invalid_id, SECRET, algorithm= JWT_ALGORITHM).decode('utf-8')


    def tearsDown(self):
        pass

    def test_success(self):

        headers ={
            'HTTP_Authorization' : self.token
        }
        response = self.client.post(self.URL, content_type='application/json', **headers)
        self.assertEqual(response.json(),{'message':'SUCCESS'})
        self.assertEquals(response.status_code, 200)


    def test_invalid_token(self):

        headers = {
            'Auth' : self.token,
        }
        response = self.client.post(self.URL, content_type='application/json', **headers)
        self.assertEqual(response.json(),{'message':'INVALID_TOKEN'})
        self.assertEquals(response.status_code, 400)

    def test_invalid_user(self):

        headers = {
            'HTTP_Authorization' : self.unknown_token
        }
        response = self.client.post(self.URL, content_type='application/json', **headers)
        self.assertEqual(response.json(),{'message':'INVALID_USER'})
        self.assertEquals(response.status_code, 400)
