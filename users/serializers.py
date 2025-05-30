from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """Класс сериализатора для создания объекта пользователя."""

    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    """Класс сериализатора для получения деталей, обновления, удаления объекта пользователя."""

    class Meta:
        model = User
        read_only_fields = ["is_active", "is_staff"]
        fields = ["id", "email", "username", "first_name", "last_name", "is_active", "is_staff"]
