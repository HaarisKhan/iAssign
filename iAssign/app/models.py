from django.db import models
from django.contrib.auth.models import User
from . import fields

# Create your models here.


class Chat(models.Model):
    username = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=250)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    boards = models.ManyToManyField(Board)


class Board(models.Model):
    people = models.ManyToManyField(Person)
    task = models.CharField(max_length=250)
    num_people = models.IntegerField()
    moderator = models.ManyToOneField(Person)
    times = fields.ListField()
    requests = fields.ListField()


class TimeSlot(models.Model):
    boards = fields.ListField()


class Requests(models.Model):
    times = fields.ListField()