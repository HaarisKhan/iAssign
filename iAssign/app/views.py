from __future__ import print_function
from django.shortcuts import render

import httplib2
import os
#
#from quickstart import get_credentials

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import json

import datetime

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
    if request.user.is_anonymous:
        return render(request, "index.html", {'request': request,
                                          'user': request.user})
    else:
        return render(request, "appPage.html", {'request': request,
                                              'user': request.user})


# def get_credentials():
#     """Gets valid user credentials from storage.
#
#     If nothing has been stored, or if the stored credentials are invalid,
#     the OAuth2 flow is completed to obtain the new credentials.
#
#     Returns:
#         Credentials, the obtained credential.
#     """
#     # If modifying these scopes, delete your previously saved credentials
#     # at ~/.credentials/calendar-python-quickstart.json
#     SCOPES = 'https://www.googleapis.com/auth/calendar'
#     CLIENT_SECRET_FILE = 'client_secret.json'
#     APPLICATION_NAME = 'Google Calendar API Python Quickstart'
#     home_dir = os.path.expanduser('~')
#     credential_dir = os.path.join(home_dir, '.credentials')
#     if not os.path.exists(credential_dir):
#         os.makedirs(credential_dir)
#     credential_path = os.path.join(credential_dir,
#                                    'calendar-python-quickstart.json')
#
#     store = Storage(credential_path)
#     credentials = store.get()
#     if not credentials or credentials.invalid:
#         flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
#         flow.user_agent = APPLICATION_NAME
#         # Needed only for compatibility with Python 2.6
#         credentials = tools.run(flow, store)
#     return credentials

try:
    import argparse

    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def DisplayCalendar(request):

    #credentials = get_credentials()
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    calendar_resource = service.calendarList().get(calendarId='primary').execute() #.list(userId='me').execute()
    extract_username = calendar_resource['summary'].split("@")
    username = extract_username[0]
    timezone = calendar_resource['timeZone']
    calendar_display = "<iframe src=\"https://calendar.google.com/calendar/embed?src="+username+"%40gmail.com&ctz="+timezone+"\" style=\"border: 0\" width=\"800\" height=\"600\" frameborder=\"0\" scrolling=\"no\"></iframe>"

    return render(request, "appPage.html", {'request': request,
                                         'user': request.user,
                                         'calendar_display': calendar_display})


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
# def getInfo():
    # Given that the user successfully logged in using Google Authentication,
    # Create a user instance and store their first and last name and email.
    # May not need to do it in this function; perhaps do it on the page they
    # authenticate instead
    return None