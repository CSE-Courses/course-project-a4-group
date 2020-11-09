from django.db import models

# Create your models here.

class singleGameMatchResult(models.Model):
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="winner")
    loser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="loser")
    pointsWagered = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=now)
    game = models.CharField(default="", max_length=100)
    modelName = models.CharField(default="singleGameMatchResult", max_length=100)
