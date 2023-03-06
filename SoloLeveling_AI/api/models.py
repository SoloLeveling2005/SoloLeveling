from django.db import models


# Create your models here.


class User(models.Model):
    # id - user_id
    username = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)


class UserBalance(models.Model):
    # id - user_balance_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance_count = models.BigIntegerField()
    tariff = models.CharField(max_length=100)


class Token(models.Model):
    # id - room_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    token_question = models.CharField(max_length=100)
    token_answer = models.CharField(max_length=100)
