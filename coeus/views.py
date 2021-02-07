from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import InstallForm, LoginForm
from .models import Settings


def index(request):
    return render(request, 'coeus/index.html')


def install(request):
    if len(User.objects.all()) > 0:
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        form = InstallForm()
    else:
        form = InstallForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            setting = Settings(settings_type='name', settings_value=form.cleaned_data['website_name'])
            setting.save()

            auth_login(request, user)
            return HttpResponseRedirect('/')

    return render(request, 'coeus/install.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/projects')

    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'You have entered an incorrect username/password.')

    return render(request, 'coeus/login.html', { 'form': form })


def logout(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    auth_logout(request)