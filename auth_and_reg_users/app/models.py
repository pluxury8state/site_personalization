from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=128, verbose_name='Логин')
    email = models.CharField(max_length=64, null=True, verbose_name='Электронная почта')
    password = models.CharField(max_length=128, verbose_name='Пароль')
    groups = None
    user_permissions = None



