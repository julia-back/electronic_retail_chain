from django.contrib import admin, messages
from .models import ChainNode, Contacts


admin.site.register(Contacts)


@admin.register(ChainNode)
class ChainNodeAdmin(admin.ModelAdmin):
    """Класс настройки звена цепи в Django Admin"""

    list_display = ["name", "contacts", "supplier", "payment_arrears", "node_type", "node_level", "created_at"]
    list_filter = ["contacts__country"]
    search_fields = ["name"]
    actions = ["clear_payment_arrears"]

    @admin.action(description="Очистить поле задолженности")
    def clear_payment_arrears(self, request, queryset):
        """Метод, определяющий admin action для очистки поля задолженности перед поставщиком выбранных объектов."""

        queryset.update(payment_arrears=0)
        self.message_user(request, "Задолженность очищена для выбранных объектов.", level=messages.SUCCESS)
