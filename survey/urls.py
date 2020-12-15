from django.urls import path

from .views import (
        SurveyResponseView,
)

urlpatterns = [
    path('/send_result', SurveyResponseView),
]
