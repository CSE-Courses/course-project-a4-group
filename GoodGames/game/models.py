from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
GAME_CHOICES = ( 
    ("Ps4", "Ps4"), 
    ("Ps4_Controller", "Ps4 controller"), 
    ("Xbox", "Xbox"), 
    ("Xbox_Controller", "Xbox controller"), 
    ("Madden", "Madden"), 
    ("Nba2k21", "Nba2k21"), 
    ("Gaming_Monitor", "Gaming Monitor"), 
    ("Gaming_Headset", "Gaming Headset"), 
)

class buyNow(models.Model):
    username = models.CharField(max_length=1024)
    fullName = models.CharField("Full name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True, null=True)
    zip_code = models.CharField("ZIP", max_length=12)
    city = models.CharField("City", max_length=1024)
    item = models.CharField( 
        max_length = 20, 
        choices = GAME_CHOICES,
        default = "Ps4"
        )
    date = models.DateTimeField(default=now)
    modelName = models.CharField(default="buyNow", max_length=100)
    

class adWatch(models.Model):
    username = models.CharField(max_length=1024)
    date = models.DateTimeField(default=now)
    modelName = models.CharField(default="adWatch", max_length=100)

class game(models.Model):
    name = models.CharField(max_length=100)

class friend(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requester")
    requestee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requestee")
    accepted = models.BooleanField(default=False)

   
