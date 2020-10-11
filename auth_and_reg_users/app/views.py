from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import User
from app.forms import UserLoginForm


def home_view(request):

    if not request.user.is_authenticated:
        return render(
            request,
            'home.html', context={'user': False}
        )
    else:
        user = request.user
        return render(request, 'home.html', context={'user': user})


def login_view(request):
    template = 'registration/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')

            else:
                form = UserLoginForm()
                error = 'Такого аккаунта нет'
                return render(request, template, context={'form': form, 'error': error})
        else:
            form = UserLoginForm()
            error = 'Не верный Пароль или Логин'
            return render(request, template, context={'form': form, 'error': error})

    form = UserLoginForm()
    return render(request, template, context={'form': form, 'errors': False},)


def logout_view(request):
    template = 'registration/logout.html'
    logout(request)
    return render(request, template, context={})


def signup_view(request):
    if request.method == 'POST':
        data = UserCreationForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('login')

    form = UserCreationForm()
    return render(request, 'registration/signup.html', context={'form': form})


