from django.urls import path
from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns = [
    path("user/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("user/new/", views.UserCreateAPIView.as_view(), name="user_create"),
    path("user/<int:pk>/", views.UserUpdateAPIView.as_view(), name="user_update"),
    path("user/<int:pk>/", views.UserDestroyAPIView.as_view(), name="user_destroy"),
]
