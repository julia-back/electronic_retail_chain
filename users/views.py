from rest_framework import generics
from .models import User
from . import serializers
from django.contrib.auth.hashers import make_password
from .permissions import IsCurrentUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomTokenObtainPairView(TokenObtainPairView):

    permission_classes = [AllowAny]


class CustomTokenRefreshView(TokenRefreshView):

    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]


class UserCreateAPIView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(
            is_active=True,
            is_staff=False,
            password=make_password(serializer.validated_data.get("password"))
        )


class UserUpdateAPIView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]


class UserDestroyAPIView(generics.DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated, IsCurrentUser]
