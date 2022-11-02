import logging

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from modules.core.web.serializers import TransactionSerializer
from modules.order_management.models.definitions import ShippingOrder, PurchaseOrder, Item


class PurchaseOrderItemSerializer:
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


class PurchaseOrderSerializer:

    class Meta:
        model = PurchaseOrder
        fields = [
            "shipping_order_id"
        ]
