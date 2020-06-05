from core.views import ListLanguages
from django.urls import path

urlpatterns = [
    path('languages/', ListLanguages.as_view()),
]
