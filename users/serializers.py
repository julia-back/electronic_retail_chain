from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        write_only_fields = ["password"]


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        read_only_fields = ["is_active", "is_staff"]
        fields = ["id", "email", "username", "first_name", "last_name", "is_active", "is_staff"]
