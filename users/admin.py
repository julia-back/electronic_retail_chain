from django.contrib import admin, messages
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "username"]
    actions = ["do_user_is_staff"]

    @admin.action(description="Присваивает пользователю статус сотрудника.")
    def do_user_is_staff(self, request, queryset):
        queryset.update(is_staff=True)
        self.message_user(request, "Выбранным пользователям присвоен статус сотрудника.", messages.SUCCESS)
