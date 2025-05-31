from rest_framework import generics
from .models import User
from . import serializers
from django.contrib.auth.hashers import make_password
from .permissions import IsCurrentUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Класс представления для получения токенов.
    Доступно неавторизованным пользователям.
    """

    permission_classes = [AllowAny]


class CustomTokenRefreshView(TokenRefreshView):
    """
    Класс представления для обновления токена.
    Доступно неавторизованным пользователям.
    """

    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс представления получения деталей пользователя.
    Доступно владельцу объекта пользователя.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]


class UserCreateAPIView(generics.CreateAPIView):
    """
    Класс представления создания пользователя.
    Доступно неавторизованным пользователям.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Переопределенный метод сохранения объекта, хеширует пароль."""

        serializer.save(
            is_active=True,
            is_staff=False,
            password=make_password(serializer.validated_data.get("password"))
        )


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Класс представления для обновления объекта пользователя.
    Доступно владельцу объекта пользователя.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Класс представления для удаления объекта пользователя.
    Доступно владельцу объекта пользователя.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]
