from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_bot = models.BooleanField()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField(max_length=4096)