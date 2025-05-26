from rest_framework import generics
from .models import User
from . import serializers
from django.contrib.auth.hashers import make_password


class UserRetrieveAPIView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = []


class UserCreateAPIView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(
            is_active=True,
            is_staff=False,
            password=make_password(serializer.validated_data.get("password"))
        )


class UserUpdateAPIView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = []


class UserDestroyAPIView(generics.DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = []
