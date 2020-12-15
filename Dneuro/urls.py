from django.urls import path, include

urlpatterns = [
    path('survey', include('survey.urls')),
]
