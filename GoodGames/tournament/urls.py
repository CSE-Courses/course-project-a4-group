from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name="newTournament"),
    path('updatescore/<int:id>', views.updateScore, name="updateScore"),
    path('<int:tid>', views.tournament, name="tournamentView"),
    
    
]
