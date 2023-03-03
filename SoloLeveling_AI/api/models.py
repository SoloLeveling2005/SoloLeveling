from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)


class Requests_history(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()

