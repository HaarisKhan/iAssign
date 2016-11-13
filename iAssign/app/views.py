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
    return HttpResponseRedirect('/login/')


def SignUp(request):
    return render(request, "create_account.html")


def Home(request):
    c = models.Chat.objects.all()
    return render(request, "index.html", {'home': 'active', 'chat': c})


def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = models.Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')


def forgot(request):
    return render(request, "forgot_password.html")

def Messages(request):
    c = models.Chat.objects.all()
    return render(request, "messages.html" , {'chat': c})

"""
<form action="#" method="get">
 <input type="datetime-local" value="" name="start_time" size="1"/>
 <input type="datetime-local" value="" name="end_time" size="1"/>
 <input type="string" placeholder="Description" name="description" size="60"/>
 <input type="submit" class="btn" value="Add Time" name="mybtn">
</form>
"""

# Create new time interval
def RequestBoardPage(request):
    board = request.GET.get('board')
    board.Create_Time_Interval()
    if request.GET.get('Add Time'):
        start_time = (request.GET.get('start_time'))
        end_time = (request.GET.get('end_time'))
        description = (request.GET.get('description'))

    return render(request, 'm/templateHTML.html', )