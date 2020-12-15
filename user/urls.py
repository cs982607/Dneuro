from django.urls import path

from .views      import SignUpView, LogInView

urlpatterns= [
    path('/signup'   , SignUpView.as_view()),
    path('/signin'   , LogInView.as_view()),
]
