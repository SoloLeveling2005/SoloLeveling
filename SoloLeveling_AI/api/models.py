from django.db import models


# Create your models here.


class User(models.Model):
    # id - user_id
    username = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_token = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)


class UserBalance(models.Model):
    # id - user_balance_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance_count = models.BigIntegerField()
    tariff = models.CharField(max_length=100)


class Token(models.Model):
    # id - room_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # todo сколько токен потребили. num_tokens(prompt) + max_tokens * max(n, best_of)
    #  -> сколько токенов подали + сколько токенов макс на вывод
    score = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
