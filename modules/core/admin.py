from django.contrib import admin

from modules.core.models.definitions import Transaction, Organization, Item, Facility

admin.site.register(Transaction)
admin.site.register(Organization)
admin.site.register(Item)
admin.site.register(Facility)
