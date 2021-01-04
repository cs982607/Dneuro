from django.urls import path

from .views      import (
    SignUpView,
    LogInView,
    Login_decoratorView,
    AuthSmsSendView,
    KakaoSignInView,
    GoogleSignInView
    )

urlpatterns= [
    path('/signup'        , SignUpView.as_view()),
    path('/signin'        , LogInView.as_view()),
    path('/test'          , Login_decoratorView.as_view()),
    path('/kakao'         , KakaoSignInView.as_view()),
    path('/google'        , GoogleSignInView.as_view()), 
    path('/sms'           , AuthSmsSendView.as_view())
]
