from rest_framework import viewsets

from ..models.definitions import ShippingOrder, PurchaseOrder, ItemInstance, Transaction
from ..web.serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer, ShippingOrderSerializer, \
    TransactionSerializer

"""Shipping Order views"""

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("id")
    serializer_class = TransactionSerializer

class ShippingOrderViewSet(viewsets.ModelViewSet):
    queryset = ShippingOrder.objects.all().order_by("id")
    serializer_class = ShippingOrderSerializer

"""Purchase Order views """

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all().order_by("id")
    serializer_class = PurchaseOrderSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemInstance.objects.all().order_by("id")
    serializer_class = PurchaseOrderItemSerializer

