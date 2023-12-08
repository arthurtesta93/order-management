from django.contrib import admin

from modules.core.models.definitions import Organization, Item, Facility, Contact, Warehouse, \
    CorporateOffice, Dock


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "kind", "yearly_revenue"]  # idea: last transaction as a column?


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "city", "state", "observations"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["commodity", "part_number"]  # last PO# shipped? number of instances?


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["get_organization", "first_name", "last_name", "email", "phone"]


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["get_dispatch_contact", "organization", "city", "state", "observations"]

admin.site.register(CorporateOffice)

@admin.register(Dock)
class DockAdmin(admin.ModelAdmin):
    list_display = ["id", "dock_label", "get_warehouse_city", "get_dispatch_contact", "refrigerated_cargo", "drop_trailer", "drayage_enabled"]
