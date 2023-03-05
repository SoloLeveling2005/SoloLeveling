from django.db import models


# Create your models here.


class User(models.Model):
    # id - user_id
    username = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)


class Room(models.Model):
    # id - room_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()

