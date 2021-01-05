from django.urls import path

from .views import (
        StartView,
        ResponseView,
        ResultView,
        ResetView,
)

urlpatterns = [
    path('/start', StartView.as_view()),
    path('/input', ResponseView.as_view()),
    path('/result', ResultView.as_view()),
    path('/reset', ResetView.as_view()),
]
