import logging

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from modules.core.web.serializers import TransactionSerializer, OrganizationSerializer
from modules.order_management.models.definitions import ShippingOrder, PurchaseOrder, Item


class PurchaseOrderItemSerializer(serializers.HyperlinkedModelSerializer):
    content = TransactionSerializer()

    class Meta:
        model = Item
        fields = [
            "purchase_order_id",
            "commodity",
            "count",
            "stackable",
            "weight",
            "dimensions",
            "type",
            "package_type",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    seller = OrganizationSerializer()
    buyer = OrganizationSerializer()
    items = PurchaseOrderItemSerializer(many=True, allow_null=True, required=False)

    def create(self, validated_data):
        items = validated_data.pop("items", [])
        root = Item.objects.create(**validated_data)
        for item in items:
            Item.objects.create(invoice=root, **item)
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
