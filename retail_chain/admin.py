from django.contrib import admin
from .models import ChainNode, Contacts


admin.site.register(Contacts)


@admin.register(ChainNode)
class ChainNodeAdmin(admin.ModelAdmin):
    list_display = ["name", "contacts", "supplier", "payment_arrears", "node_type", "node_level", "created_at"]
    list_filter = ["contacts__country"]
    search_fields = ["name"]
