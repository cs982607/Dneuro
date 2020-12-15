from django.urls import path

from .views      import (
    SignUpView,
    LogInView,
    Login_decoratorView
    )

urlpatterns= [
    path('/signup'   , SignUpView.as_view()),
    path('/signin'   , LogInView.as_view()),
    path('/test'     , Login_decoratorView.as_view()),
]
