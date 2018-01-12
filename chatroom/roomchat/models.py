from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# Create your models here.
class RoomChat(models.Model):
    participants = models.ManyToManyField(User, related_name='chatrooms')
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='owned_rooms')

    def __str__(self):
        return self.title


class Message(models.Model):
    roomchat = models.ForeignKey(RoomChat, models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(auto_now_add=True)
