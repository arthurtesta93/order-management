from django.contrib import admin

from modules.core.models.definitions import Transaction, Organization

admin.site.register(Transaction)
admin.site.register(Organization)
