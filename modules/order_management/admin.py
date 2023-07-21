from django.contrib import admin

from ..order_management.models.definitions import PurchaseOrder, ItemInstance, ShippingOrder

@admin.register(ShippingOrder)
class ShippingOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "pickup_date", "delivery_date", "get_ship_from", "get_ship_to"]


#admin.site.register(ShippingOrder, ShippingOrderAdmin)
admin.site.register(PurchaseOrder)
admin.site.register(ItemInstance)
# Register your models here.
