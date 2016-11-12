from django.db import models
from django.contrib.auth.models import User
#from . import fields


class Chat(models.Model):
    username = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=250)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    boards = models.ManyToManyField(Board)
    email = models.CharField(max_length=250)


class Organization(models.Model):
    users = models.ManyToManyField(Person)
    boards = models.OneToManyField(Board)
    org_name = models.CharField(max_length=250)


class Board(models.Model):
    people = models.ManyToManyField(Person)
    task = models.CharField(max_length=250)
    num_people = models.IntegerField()
    moderator = models.ManyToManyField(Person)
    times = models.ManyToManyField(TimeIntervalObject)
    requests = models.ForeignKey(Requests)


class TimeIntervalObject(models.Model):
    boards = models.ManyToManyField(Board)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    people = models.ManyToManyField(Person)


class Requests(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    original_time = models.OneToOneField(TimeIntervalObject)
    original_person = models.OneToOneField(Person)
    end_time = models.OneToOneField(TimeIntervalObject)
    end_person = models.OneToOneField(Person)
    original_person_approval = models.BooleanField
    end_person_approval = models.BooleanField

