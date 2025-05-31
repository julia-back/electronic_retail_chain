from django.urls import path
from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns = [
    path("token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", views.CustomTokenRefreshView.as_view(), name="token_refresh"),

    path("user/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("user/new/", views.UserCreateAPIView.as_view(), name="user_create"),
    path("user/<int:pk>/update/", views.UserUpdateAPIView.as_view(), name="user_update"),
    path("user/<int:pk>/delete/", views.UserDestroyAPIView.as_view(), name="user_destroy"),
]
