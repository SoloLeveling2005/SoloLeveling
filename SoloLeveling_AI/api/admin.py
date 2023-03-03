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
        'token'
    )
    list_display_links = (
        'id',
        'username',
        'password',
        'token'
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'username',
        'password',
        'token'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'username',
            'password',
            'token'
        )}),
    )
    search_fields = [
        'id',
        'username',
        'password',
        'token'
    ]


admin.site.register(models.User, User)



class Requests_history(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'id',
        'user_id',
        'data',
    )
    list_display_links = (
        'id',
        'user_id',
        'data',
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'user_id',
        'data',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'user_id',
            'data',
        )}),
    )
    search_fields = [
        'id',
        'user_id',
        'data',
    ]


admin.site.register(models.Requests_history, Requests_history)
