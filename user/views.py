import(
    json,
    jwt,
    re,
    bcrypt
)

from django.views     import View
from django.http      import JsonResponse

from .models          import(
    User,
    Country
    )
from my_settings      import (
    SECRET,
    JWT_ALGORITHM
    )
from .utils           import Login_decorator

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            email_pattern    = '[a-zA-Z0-9_-]+@[a-z]+.[a+z]'
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


