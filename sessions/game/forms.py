from django import forms
from django.contrib.auth import models

from .models import PlayerGameInfo, Game


class PlayerGameInfoForm(forms.ModelForm):

    count = forms.IntegerField(label='Таинственное число')

    class Meta:
        model = Game

        fields = ['count']


class PlayerTryForm(forms.ModelForm):

    guess_count = forms.IntegerField(label='Предположительное число')

    class Meta:
        model = Game
        fields = ['guess_count']