from django.urls import path
from . import views

urlpatterns = [
    path('', views.gameMatchResult, name='gameMatchResult-form'),
]
