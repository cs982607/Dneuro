import json, jwt, re
import bcrypt
from django.test import TestCase, Client
from django.http import JsonResponse

import my_settings

from .models     import User, Country


class UserTestCase(TestCase):
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

    def test_signup_invalid_eail(self):

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

