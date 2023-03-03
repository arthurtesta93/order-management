from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models.definitions import ShippingOrder, PurchaseOrder, ItemInstance
from ..web.serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer, ShippingOrderSerializer

"""Shipping Order views"""


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

