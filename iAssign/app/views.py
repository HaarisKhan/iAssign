from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.urls import reverse

from . import models

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'main/login.html')

    return render_to_response('main/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



def message(request):
    c = models.Chat.objects.all()
    return render(request, 'main/messages.html', {'chat': c})