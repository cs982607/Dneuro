import json, jwt, re, bcrypt

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse

class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']

            email_pattern = '[a-zA-Z0-9_-]+@[a-z]+.[a+z]+'
            password_pattern = '[A-Za-z0-9!@#$%^&*]'

            if not re.match(email_pattern, email):
                return JsonResponse({'message':'INVALID_EMAIL'}, status=400)
            if not re.search(password_pattern, password)or len(password)>16 or len(password)<8:
                return JsonResponse({'message':'INVALID_PASSWORD'}, status=400)

            

