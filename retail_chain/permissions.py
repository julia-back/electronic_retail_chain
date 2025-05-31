from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """Класс разрешения, проверяет, является ли текущий авторизованный пользователь сотрудником."""

    def has_permission(self, request, view):
        return request.user.is_staff is True
