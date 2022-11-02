from django.contrib import admin

from ..order_management.models.definitions import PurchaseOrder, Item

admin.site.register(PurchaseOrder)
admin.site.register(Item)
# Register your models here.
