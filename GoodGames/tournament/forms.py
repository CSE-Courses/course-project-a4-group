from django import forms
from .models import tournament
from django.forms import ModelForm

class NewTournamentForm(ModelForm):
    class Meta:
        model = tournament
        fields = [
            'name','no_of_players', 'start_date', 'game'
            ]