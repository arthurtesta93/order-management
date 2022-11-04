from django.contrib import admin

from ..order_management.models.definitions import PurchaseOrder, Item, ShippingOrder

admin.site.register(ShippingOrder)
admin.site.register(PurchaseOrder)
admin.site.register(Item)
# Register your models here.
