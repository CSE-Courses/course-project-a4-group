from django.db import models
from django.contrib.auth.models import User
from game.models import game

# Create your models here.

class tournament(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="creator")
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    no_of_players = models.IntegerField()
    game = models.ForeignKey(game, on_delete=models.SET_NULL, null=True, related_name="game")
    completed = models.BooleanField()

class registration(models.Model):
    player = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="player")
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE, related_name="tournament")

class tournamentMatch(models.Model):
    tourn_id = models.ForeignKey(tournament, on_delete=models.CASCADE)
    p1 = models.ForeignKey(registration, on_delete=models.SET_NULL, null=True, related_name="p1")
    p2 = models.ForeignKey(registration, on_delete=models.SET_NULL, null=True, related_name="p2")
    winner = models.ForeignKey(registration, on_delete=models.SET_NULL, null=True, related_name="match_winner")
    game_no = models.IntegerField()
