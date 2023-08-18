from rest_framework import viewsets

from ..models.definitions import ShippingOrder, PurchaseOrder, ItemInstance, Transaction
from ..web.serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer, ShippingOrderSerializer, \
    TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("id")
    serializer_class = TransactionSerializer


"""Shipping Order views"""


class ShippingOrderViewSet(viewsets.ModelViewSet):
    queryset = ShippingOrder.objects.all().order_by("id")
    serializer_class = ShippingOrderSerializer


class ShippingOrderPurchaseOrdersViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all().order_by("id")
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        shipping_order_id = self.request.query_params.get("id", None)
        if shipping_order_id is not None:
            return PurchaseOrder.objects.filter(shipping_order_id=shipping_order_id)
        return PurchaseOrder.objects.filter(shipping_order_id=self.kwargs['shipping_order_id'])

"""Purchase Order views """


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all().order_by("id")
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderItemsViewSet(viewsets.ModelViewSet):
    queryset = ItemInstance.objects.all().order_by("id")
    serializer_class = PurchaseOrderItemSerializer

    def get_queryset(self):
        purchase_order_id = self.request.query_params.get("id", None)
        if purchase_order_id is not None:
            return ItemInstance.objects.filter(purchase_order_id=purchase_order_id)
        return ItemInstance.objects.filter(purchase_order_id=self.kwargs['purchase_order_id'])


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemInstance.objects.all().order_by("id")
    serializer_class = PurchaseOrderItemSerializer
