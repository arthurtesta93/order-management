from django.contrib import admin

from modules.core.models.definitions import Transaction, Organization, Item, Facility, Storage, Contact, Warehouse, \
    CorporateOffice, Dock

admin.site.register(Transaction)
admin.site.register(Organization)
admin.site.register(Item)
admin.site.register(Facility)
admin.site.register(Storage)
admin.site.register(Contact)
admin.site.register(Warehouse)
admin.site.register(CorporateOffice)
admin.site.register(Dock)
