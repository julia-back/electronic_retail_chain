from rest_framework.permissions import BasePermission


class IsCurrentUser(BasePermission):
    """Класс разрешения, проверяет, получает ли текущий авторизованный пользователь свой объект пользователя."""

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
