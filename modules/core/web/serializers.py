import logging

from rest_framework import serializers

from ..models.definitions import Item, Organization, Facility, CorporateOffice, Warehouse, Dock, \
    Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

        read_only_fields = ["id", "url", "created_at", "updated_at"]

    def validate(self, data):
        if data["first_name"] == "":
            raise serializers.ValidationError("First name cannot be empty")
        if data["last_name"] == "":
            raise serializers.ValidationError("Last name cannot be empty")
        if data["email"] == "":
            raise serializers.ValidationError("Email cannot be empty")
        if data["phone"] == "":
            raise serializers.ValidationError("Phone cannot be empty")
        if data["organization"] == "":
            raise serializers.ValidationError("Organization cannot be empty")
        return data


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ["id", "url", "created_at", "updated_at"]

    def validate(self, data):
        if data["weight"] <= "0":
            raise serializers.ValidationError("Weight must be greater than 0")
        if data["count"] <= 0:
            raise serializers.ValidationError("Count must be greater than 0")
        if data["height_package_unit"] <= 0:
            raise serializers.ValidationError("Height must be greater than 0")
        if data["width_package_unit"] <= 0:
            raise serializers.ValidationError("Width must be greater than 0")
        if data["length_package_unit"] <= 0:
            raise serializers.ValidationError("Length must be greater than 0")
        if data["part_number"] == "":
            raise serializers.ValidationError("Part Number cannot be empty")
        if data["commodity"] == "":
            raise serializers.ValidationError("Commodity cannot be empty")

        return data


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name", "kind", "yearly_revenue", "created_at", "updated_at", "url"]
        read_only_fields = ["id", "created_at", "updated_at"]


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'
        read_only_fields = ["id"]

    def validate(self, data):
        if data["name"] == "":
            raise serializers.ValidationError("Name cannot be empty")
        if data["zip_code"] == "":
            raise serializers.ValidationError("Zip code cannot be empty")
        if data["street"] == "":
            raise serializers.ValidationError("Street cannot be empty")
        if data["street_number"] <= 0:
            raise serializers.ValidationError("Street number must be greater than 0")
        if data["city"] == "":
            raise serializers.ValidationError("City cannot be empty")
        if data["state"] == "":
            raise serializers.ValidationError("State cannot be empty")
        if data["country"] == "":
            raise serializers.ValidationError("Country cannot be empty")
        if data['working_days'] is None:
            raise serializers.ValidationError("Working days cannot be empty")
        return data


class CorporateOfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CorporateOffice
        fields = '__all__'
        read_only_fields = ["id"]


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
        read_only_fields = ["id"]

    def validate(self, data):
        if data["allow_repackaging_until_appointment"] and \
                data["time_allowed_for_repackaging_before_appointment"] is None:
            raise serializers.ValidationError("If repackaging is allowed, a time must be specified")


class DockSerializer(serializers.HyperlinkedModelSerializer):
    dock_dispatch_contact = Contact()  # <- Need to make iterable

    class Meta:
        model = Dock
        fields = '__all__'
        read_only_fields = ["id"]

    def validate(self, data):
        if data["appointment_slot_time_hours"] <= 0:
            raise serializers.ValidationError("Appointment slot time must be greater than 0")
        if data["dock_label"] == "":
            raise serializers.ValidationError("Dock label cannot be empty")
        return data
