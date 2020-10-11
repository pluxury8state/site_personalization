from app.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        password = forms.PasswordInput()
        fields = ['username', 'password']
