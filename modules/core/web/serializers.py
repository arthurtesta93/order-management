import logging

from rest_framework import serializers

from ..models.definitions import Item, Organization, Facility, CorporateOffice, Warehouse, Dock, \
    Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "phone", "organization", "observations"]

        read_only_fields = ["id", "url", "created_at", "updated_at"]


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "part_number", "commodity", "count", "package_type", "weight", "weight_package_unit",
                  "height_package_unit", "width_package_unit", "length_package_unit", "dimension_unit",
                  "hazardous", "temperature_controlled"]
        read_only_fields = ["id", "url", "created_at", "updated_at"]


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name", "kind", "yearly_revenue", "created_at", "updated_at", "url"]
        read_only_fields = ["id", "created_at", "updated_at"]


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "organization", "working_days", "name", "url", "zip_code", "street", "street_number", "city",
                  "state",
                  "country", "observations"]
        read_only_fields = ["id"]


class CorporateOfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CorporateOffice
        fields = ["id", "organization", "name", "url", "zip_code", "street", "street_number", "city", "state",
                  "country", "observations", "contact", "billable"]
        read_only_fields = ["id"]


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["id", "organization", "name", "url", "zip_code", "street", "street_number", "city", "state",
                  "country", "observations", "dispatch_contact", "free_reschedule_enabled",
                  "allow_repackaging_until_appointment", "time_allowed_for_repackaging_before_appointment",
                  "detention_daily_cost", "warehouse_label"]
        read_only_fields = ["id"]


class DockSerializer(serializers.HyperlinkedModelSerializer):
    dock_dispatch_contact = ContactSerializer(required=False)  # <- Need to make iterable

    class Meta:
        model = Dock
        fields = ["warehouse", "dock_dispatch_contact", "refrigerated_cargo", "drop_trailer",
                  "refrigerated_cargo", "drayage_enabled", "live_load", "hazmat"]
#        depth = 1
