from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import buyNow
from django.forms import ModelForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class buyNowForm(ModelForm):
    class Meta:
        model = buyNow
        fields = [
            'name', 'address1', 'address2', 'zip_code', 'city'
            ]
