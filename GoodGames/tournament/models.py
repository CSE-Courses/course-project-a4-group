from django.db import models
from django.contrib.auth.models import User
from game.models import game
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class tournament(models.Model):

    player_count = (
        (4,4),
        (8,8),
        (16,16),
        (32,32)
    )

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="creator")
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None, related_name="tournament_winner")
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    no_of_players = models.IntegerField(choices=player_count)
    game = models.ForeignKey(game, on_delete=models.SET_NULL, null=True, related_name="game")
    completed = models.BooleanField(default=False)
    started = models.BooleanField(default=False)
    wager = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class registration(models.Model):
    player = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="player")
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE, related_name="tournament")

    def __str__(self):
        return self.player.username + ' in ' + self.tournament.name

class tournamentMatch(models.Model):
    tourn_id = models.ForeignKey(tournament, on_delete=models.CASCADE)
    p1 = models.ForeignKey(registration, on_delete=models.SET_NULL, null=True, related_name="p1")
    p2 = models.ForeignKey(registration, on_delete=models.SET_NULL, null=True, related_name="p2")
    winner = models.ForeignKey(registration, on_delete=models.SET_NULL, null=True, related_name="match_winner")
    bracketNo = models.IntegerField()
    lastGames = ArrayField(models.IntegerField(), null=True, default=[])
    nextGame = models.IntegerField(null=True, default=0)
    roundNo = models.IntegerField(null=True, default=0)
    bye = models.BooleanField(default=False)
    teamnames = ArrayField(models.CharField(max_length=200), null=True, default=[])
    
