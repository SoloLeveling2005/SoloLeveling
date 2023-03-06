from django.contrib import admin
from api import models


class User(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'id',
        'username',
        'password',
        'user_token',
        'created_at'
    )
    list_display_links = (
        'id',
        'username',
        'password',
        'user_token',
        'created_at'
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'username',
        'password',
        'user_token',
        'created_at'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'username',
            'password',
            'user_token',
        )}),
    )
    search_fields = [
        'id',
        'username',
        'password',
        'user_token',
        'created_at'
    ]


admin.site.register(models.User, User)


class UserBalance(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'id',
        'user_id',
        'balance_count',
        'tariff'
    )
    list_display_links = (
        'id',
        'user_id',
        'balance_count',
        'tariff'
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'user_id',
        'balance_count',
        'tariff'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'user_id',
            'balance_count',
            'tariff'
        )}),
    )
    search_fields = [
        'id',
        'user_id',
        'balance_count',
        'tariff'
    ]


admin.site.register(models.UserBalance, UserBalance)


class Token(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'id',
        'user_id',
        'score',
        'created_at'
    )
    list_display_links = (
        'id',
        'user_id',
        'score',
        'created_at'
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'user_id',
        'score',
        'created_at'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'user_id',
            'score',
        )}),
    )
    search_fields = [
        'id',
        'user_id',
        'score',
        'created_at'
    ]


admin.site.register(models.Token, Token)
