"""Конфигурация приложения API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """class для приложения API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
