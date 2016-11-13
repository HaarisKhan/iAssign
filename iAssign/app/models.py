from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)


class Person(models.Model):
    username = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    boards = []
    #email = models.CharField(max_length=250)


class TimeIntervalObject(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=250)


class Request(models.Model):
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    original_time = models.OneToOneField(TimeIntervalObject, related_name="start")
    original_person = models.OneToOneField(Person)
    end_time = models.OneToOneField(TimeIntervalObject)
    end_person = models.OneToOneField(Person, related_name="approval")
    original_person_approval = models.BooleanField()
    end_person_approval = models.BooleanField()


class Board(models.Model):
    #people = models.ManyToManyField(Person, related_name="users")
    #task = models.CharField(max_length=250)
    #num_people = models.IntegerField()
    #requests = models.ForeignKey(Request, related_name="requests")
    times = set()
    requests = set()
    users = set()

    def addPerson(self, person):
        if type(person) == Person:
            if person not in self.users:
                self.users.add(person)
        

    def removePerson(self, person):
        if type(person) == Person:
            if person in self.users:
                self.users.remove(person)


    def addTimeInterval(self, interval):
        if type(interval) == TimeIntervalObject:
            if interval not in self.times:
                self.times.add(interval)

    def removeTimeInterval(self, interval):
        if type(interval) == TimeIntervalObject:
            if interval in self.times:
                self.times.remove(interval)


class Organization(models.Model):
    users = models.ManyToManyField(Person)
    boards = models.ForeignKey(Board, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=250)

