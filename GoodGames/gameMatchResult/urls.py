from django.urls import path
from . import views

urlpatterns = [
    path('gameMatchResult', views.gameMatchResult, name='gameMatchResult-form'),
]
