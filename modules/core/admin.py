from django.contrib import admin

from modules.core.models.definitions import Transaction, Organization, Item

admin.site.register(Transaction)
admin.site.register(Organization)
admin.site.register(Item)
