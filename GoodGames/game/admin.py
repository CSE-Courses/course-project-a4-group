from django.contrib import admin
from .models import buyNow, game, adWatch, friend

# Register your models here.

admin.site.register(buyNow)
admin.site.register(adWatch)
admin.site.register(game)
admin.site.register(friend)
