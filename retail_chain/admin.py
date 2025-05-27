from django.contrib import admin, messages
from .models import ChainNode, Contacts


admin.site.register(Contacts)


@admin.register(ChainNode)
class ChainNodeAdmin(admin.ModelAdmin):
    list_display = ["name", "contacts", "supplier", "payment_arrears", "node_type", "node_level", "created_at"]
    list_filter = ["contacts__country"]
    search_fields = ["name"]
    actions = ["clear_payment_arrears"]

    @admin.action(description="Очистить поле задолженности")
    def clear_payment_arrears(self, request, queryset):
        queryset.update(payment_arrears=0)
        self.message_user(request, "Задолженность очищена для выбранных объектов.", level=messages.SUCCESS)
