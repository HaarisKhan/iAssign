from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Chat(models.Model):
    username = models.ForeignKey(User)
    create = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=250)

