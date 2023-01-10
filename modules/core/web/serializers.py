import logging

from rest_framework import serializers

from ..models.definitions import Transaction, Organization, Facility


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


class OrganizationSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name", "url"]
        read_only_fields = ["id"]


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name", "url"]
        read_only_fields = ["id"]
