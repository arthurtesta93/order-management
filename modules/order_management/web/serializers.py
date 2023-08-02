from rest_framework import serializers

from modules.order_management.models.definitions import ShippingOrder, PurchaseOrder, ItemInstance, Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "kind", "created_at", "updated_at", "url"]
        read_only_fields = ["id", "url", "created_at", "updated_at"]


class PurchaseOrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemInstance
        fields = [
            "purchase_order_id",
            "special_instructions",
            "quantity",
            "item"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = [
            "shipping_order_id",
            "seller",
            "buyer",
            "purchase_order_status"
        ]


class ShippingOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingOrder
        fields = [
            "mode",
            "date_received",
            "pickup_date",
            "delivery_date",
            "customer_reference",
            "carrier",
            "bill_to",
            "ship_from",
            "ship_to",
            "shipping_order_status",
            "url"
        ]
        read_only_fields = ["id", "created_at", "updated_at", "deleted_at"]



