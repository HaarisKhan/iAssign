from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.urls import reverse

from iAssign import settings
from . import models


# Create your views here.


def ThirdAuthLogin(request):
    return render(request, "index.html", {'request': request,
                                          'user': request.user})


def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "login.html", {'next': next})


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def SignUp(request):
    return render(request, "create_account.html")


def Home(request):
    c = models.Chat.objects.all()
    return render(request, "index.html", {'home': 'active', 'chat': c})


def forgot(request):
    return render(request, "forgot_password.html")


def calendar(request):
    if request.POST:
        print(request.POST)

        if 'start_time' in request.POST:
            startTime = request.POST['start_time']
            endTime = request.POST['end_time']
            description = request.POST['description']

            if startTime and endTime and description:
                models.TimeIntervalObject.objects.create(start_time=startTime, end_time=endTime, description=description)
                timeInterval.save()

        elif 'chat-msg' in request.POST:
            chat = models.Chat.objects.create(message=request.POST.get('chat-msg'))
            print(request.POST.get('chat-msg'))
            print(chat)
            if chat is not None:
                chat.save()
                c = models.Chat.objects.all()
                print(c)
                return render(request, "appPage.html", {'chat': c})

    return render(request, "appPage.html")


def getInfo():
    # Given that the user successfully logged in using Google Authentication,
    # Create a user instance and store their first and last name and email.
    # May not need to do it in this function; perhaps do it on the page they
    # authenticate instead
    return None