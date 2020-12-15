from django.urls import path

from .views import (
        SurveyStartView,
        SurveyResponseView,
)

urlpatterns = [
    path('/start', SurveyStartView.as_view()),
    path('/input', SurveyResponseView.as_view()),
]
