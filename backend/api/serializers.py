"""Сериалайзер для приложения API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Task."""

    class Meta:
        """Meta class для TaskSerializer configuration."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
