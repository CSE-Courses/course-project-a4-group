from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(default=None, null=True)

    balance = models.IntegerField(default=100000)

    address = models.CharField(max_length=100, default=None, null=True)
    city = models.CharField(max_length=100, default=None, null=True)
    state = models.CharField(max_length=2, default=None, null=True)
    zip_code = models.CharField(max_length=5, default=None, null=True)
    
    

    