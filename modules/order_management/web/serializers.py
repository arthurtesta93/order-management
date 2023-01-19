import logging

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from modules.core.web.serializers import OrganizationSerializer
from modules.order_management.models.definitions import ShippingOrder, PurchaseOrder, ItemInstance


class PurchaseOrderItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ItemInstance
        fields = [
            "purchase_order_id",
            "serial_number",
            "special_instructions",
            "part_number",
            "commodity",
            "count",
            "package_type",
            "weight_package_unit",
            "height_package_unit",
            "width_package_unit",
            "length_package_unit",
            "dimension_unit",
            "hazardous",
            "temperature_controlled"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    seller = OrganizationSerializer()
    buyer = OrganizationSerializer()
    items = PurchaseOrderItemSerializer(many=True, allow_null=True, required=False)

    def create(self, validated_data):
        items = validated_data.pop("items", [])
        root = ItemInstance.objects.create(**validated_data)
        for item in items:
            ItemInstance.objects.create(invoice=root, **item)
        return root

    class Meta:
        model = PurchaseOrder
        fields = [
            "shipping_order_id",
            "seller",
            "buyer",
            "items",
        ]


class ShippingOrderSerializer:
    class Meta:
        model = ShippingOrder
        fields = [
            "mode",
            "date_received",
            "last_update",
            "pickup_date",
            "delivery_date"
        ]
