from django.contrib import admin

from ..order_management.models.definitions import PurchaseOrder, ItemInstance, ShippingOrder

admin.site.register(ShippingOrder)
admin.site.register(PurchaseOrder)
admin.site.register(ItemInstance)
# Register your models here.
