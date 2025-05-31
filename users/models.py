from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Класс модели пользователя.
    Определяет поле email в качестве поля авторизации.
    """

    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        """Метод строкового отображения пользователя."""

        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["last_name", "first_name"]
