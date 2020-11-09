from django import forms
from .models import singleGameMatchResult
from django.forms import ModelForm

class singleGameMatchResultForm(ModelForm):
    class Meta:
        model = singleGameMatchResult
        fields = [
            'winner', 'loser', 'pointsWagered', 'game'
            ]