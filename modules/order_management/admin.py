from django.contrib import admin

from ..order_management.models.definitions import PurchaseOrder, ItemInstance, ShippingOrder

@admin.register(ShippingOrder)
class ShippingOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "pickup_date", "delivery_date", "get_ship_from", "get_ship_to"]

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "get_buyer", "get_seller", "purchase_order_status"]

@admin.register(ItemInstance)
class ItemInstanceAdmin(admin.ModelAdmin):
    list_display = ["id", "get_commodity", "quantity", "purchase_order_id"]
