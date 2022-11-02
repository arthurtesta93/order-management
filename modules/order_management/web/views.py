from django.shortcuts import render

from rest_framework import viewsets

from ..models.definitions import ShippingOrder, PurchaseOrder, Item
from ..web.serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all().order_by("id")
    serializer_class = PurchaseOrderSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("id")
    serializer_class = PurchaseOrderItemSerializer
