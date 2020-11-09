from django.contrib import admin
from .models import tournament, registration, tournamentMatch

# Register your models here.

admin.site.register(tournament)
admin.site.register(registration)
admin.site.register(tournamentMatch)
