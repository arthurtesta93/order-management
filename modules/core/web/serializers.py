import logging

from rest_framework import serializers

from ..models.definitions import Item, Transaction, Organization, Facility, CorporateOffice, Storage, Warehouse, Dock, \
    Contact


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "part_number", "commodity", "count", "package_type", "weight_package_unit",
                  "height_package_unit", "width_package_unit", "length_package_unit", "dimension_unit",
                  "hazardous", "temperature_controlled"]
        read_only_fields = ["id", "url", "created_at", "updated_at"]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "kind", "created_at", "updated_at", "url"]
        read_only_fields = ["id", "url", "created_at", "updated_at"]

    def _read_only_defaults(self):
        logging.error(self.context["request"].data)
        return super(TransactionSerializer, self)._read_only_defaults()


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name", "kind", "created_at", "updated_at", "url"]
        read_only_fields = ["id", "created_at", "updated_at"]


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "organization", "name", "url", "zip_code", "street", "street_number", "city", "state",
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
                  "detention_daily_cost"]
        read_only_fields = ["id"]


class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = ["id", "organization", "name", "url", "zip_code", "street", "street_number", "city", "state",
                  "country", "observations", "working_hour_start", "working_hour_end", "working_days",
                  "refrigerated_storage", "drop_trailer", "dispatch_contact", "contact"]
        read_only_fields = ["id"]


class DockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dock
        fields = ["warehouse", "dock_dispatch_contact", "working_hour_start", "working_hour_end", "working_days",
                  "refrigerated_cargo", "drop_trailer", "drayage_enabled", "live_load", "hazmat"]


