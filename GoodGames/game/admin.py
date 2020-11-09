from django.contrib import admin
from .models import buyNow, game, adWatch

# Register your models here.

admin.site.register(buyNow)
admin.site.register(adWatch)
admin.site.register(game)
