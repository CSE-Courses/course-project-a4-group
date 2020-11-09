from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(default=None, null=True, blank=True)

    balance = models.IntegerField(default=100000)

    address = models.CharField(max_length=100, default=None, null=True, blank=True)
    city = models.CharField(max_length=100, default=None, null=True, blank=True)
    state = models.CharField(max_length=2, default=None, null=True, blank=True)
    zip_code = models.CharField(max_length=5, default=None, null=True, blank=True)

    steam_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    youtube_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    avatar_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    facebook_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    
    

    