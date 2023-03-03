from rest_framework import serializers

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
    items = PurchaseOrderItemSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = PurchaseOrder
        fields = [
            "shipping_order_id",
            "seller",
            "buyer",
            "items",
        ]


class ShippingOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingOrder
        fields = [
            "mode",
            "date_received",
            "pickup_date",
            "delivery_date",
            "reference",
            "carrier",
            "bill_to",
            "ship_from",
            "ship_to",
            "shipping_order_status",
            "url"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]



