import json, jwt, re, bcrypt, requests

from random           import randint
from django.views     import View
from django.http      import JsonResponse
from django.shortcuts import redirect

from .models          import(
    User,
    Country,
    AuthSms
    )
from my_settings      import (
    SECRET,
    JWT_ALGORITHM,
    SMS_ACCESS_KEY_ID,
    SMS_SERVICE_SECRET,
    SMS_SEND_PHONE_NUMBER,
    SMS_URL,
    KAKAO_REST_API
    )
from .utils           import Login_decorator

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            email_pattern    = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            password_pattern = '[A-Za-z0-9!@#$%^&*]'

            if not re.match(email_pattern, email):
                return JsonResponse({'message':'INVALID_EMAIL'}, status=400)
            if not re.search(password_pattern, password)or len(password)>16 or len(password)<8:
                return JsonResponse({'message':'INVALID_PASSWORD'}, status=400)

            if User.objects.filter(email=email):
                return JsonResponse({'message':'ALREADY_EMAIL'}, status=400)
            if data['country']=='대한민국' or data['country']=='KOREA':
                country_id = 1

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            user = User.objects.create(
               email      = email,
               password   = hashed_password,
               sex        = data['sex'],
               birthday   = data['birthday'],
               country_id = country_id
           )
            return JsonResponse({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            user = User.objects.get(email=email)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'email':email}, SECRET, algorithm=JWT_ALGORITHM).decode('utf-8')

                return JsonResponse({'token':token}, status=200)
            return JsonResponse({'message':'INVALID_PASSWORD'}, status=400)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message':'USER_DOES_NOT_EXIST'}, status=400)


class Login_decoratorView(View):
    @Login_decorator
    def post(self, request):
        return JsonResponse({'message':'SUCCESS'}, status=200)

class AuthSmsSendView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            phone_number        = data['phone_number']
            AuthSms.objects.update_or_create(phone_number = phone_number)

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    def get(self, request):
        try:
            phone_number = request.GET.get('phone_number', '')
            auth_number  = request.GET.get('auth_number', 0)
            result       = AuthSms.check_auth_number(phone_number, auth_number)

            return JsonResponse({'message': 'SUCCESS', 'result': result}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class KakaoSignInView(View):
    def post(self, request):
        try:
            token    = request.headers['Authorization']
            profile  = requests.post("https://kapi.kakao.com/v2/user/me", headers= {"Authorization" : f"Bearer {token}"})

            profile  = profile.json()
            kakao_id = profile.get('id', None)

            if not kakao_id:
                return JsonResponse({'message':'INVALID_TOKEN'}, status=400)

            kakao_account = profile.get("kakao_account")
            email         = profile.get("email", '')

            if User.objects.filter(kakao_id = kakao_id).exists():
                user  = User.objects.get(kakao_id=kakao_id)
                token = jwt.encode({"user_id":user.id}, SECRET, algorithm=JWT_ALGORITHM).decode("utf-8")
                return JsonResponse({"token":token}, status=200)

            user = User.objects.create(
                kakao_id = kakao_id,
                email    = email
            )
            token = jwt.encode({"user_id":user.id}, SECRET, algorithm=JWT_ALGORITHM).decode("utf-8")

            return JsonResponse({"token":token}, status=200)

        except  KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)


class GoogleSignInView(View):
    def post(self, request):
        try:
            token    = request.headers['Authorization']
            profile  = requests.post("https://kapi.kakao.com/v2/user/me", headers= {"Authorization" : f"Bearer {token}"})

            profile  = profile.json()
            kakao_id = profile.get('id', None)

            if not kakao_id:
                return JsonResponse({'message':'INVALID_TOKEN'}, status=400)

            kakao_account = profile.get("kakao_account")
            email         = profile.get("email", '')

            if User.objects.filter(kakao_id = kakao_id).exists():
                user  = User.objects.get(kakao_id=kakao_id)
                token = jwt.encode({"user_id":user.id}, SECRET, algorithm=JWT_ALGORITHM).decode("utf-8")
                return JsonResponse({"token":token}, status=200)

            user = User.objects.create(
                kakao_id = kakao_id,
                email    = email
            )
            token = jwt.encode({"user_id":user.id}, SECRET, algorithm=JWT_ALGORITHM).decode("utf-8")

            return JsonResponse({"token":token}, status=200)

        except  KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
