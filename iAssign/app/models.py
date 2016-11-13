from django.db import models
from django.contrib.auth.models import User
#from . import fields


class Chat(models.Model):
    username = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=250)


"""
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #boards = models.ManyToManyField(Board)


# class Board(models.Model):
#     people = models.ManyToManyField(Person)
#     task = models.CharField(max_length=250)
#     num_people = models.IntegerField()
#     moderator = models.ManyToManyField(Person)
#     times = models.ManyToManyField(TimeSlot)
#     # requests = models.ForeignKey(Requests)
#
#
# class TimeSlot(models.Model):
#     boards = models.ManyToManyField(Board)
#
#
# class Requests(models.Model):
#     board = models.ForeignKey(Board, on_delete=models.CASCADE)
#     #times = models.
#

"""

