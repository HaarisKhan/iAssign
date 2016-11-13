from django.db import models
from django.contrib.auth.models import User, AbstractUser


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
    boards = models.ForeignKey(Board, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=250)


class Board(models.Model):
    people = models.ManyToManyField(Person)
    task = models.CharField(max_length=250)
    num_people = models.IntegerField()
    moderator = models.ManyToManyField(Person)
    times = models.ForeignKey(TimeIntervalObject, on_delete=models.CASCADE)
    requests = models.ForeignKey(Request)

    # Create new time interval
    def Create_Time_Interval(self):
        return None


class TimeIntervalObject(models.Model):
    boards = models.OneToOneField(Board)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    people = models.ManyToManyField(Person)


class Request(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    original_time = models.OneToOneField(TimeIntervalObject)
    original_person = models.OneToOneField(Person)
    end_time = models.OneToOneField(TimeIntervalObject)
    end_person = models.OneToOneField(Person)
    original_person_approval = models.BooleanField()
    end_person_approval = models.BooleanField()
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
