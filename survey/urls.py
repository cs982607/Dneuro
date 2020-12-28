from django.urls import path

from .views import (
        StartView,
        ResponseView,
        ResultView,
)

urlpatterns = [
    path('/start', StartView.as_view()),
    path('/input', ResponseView.as_view()),
    path('/result', ResultView.as_view()),
]
