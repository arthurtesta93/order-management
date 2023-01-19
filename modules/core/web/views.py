from django.shortcuts import render

from rest_framework import viewsets

from ..models.definitions import Transaction, Organization, Facility, Item, CorporateOffice, Warehouse, Storage, Dock
from ..web.serializers import TransactionSerializer, OrganizationSerializer, FacilitySerializer, ItemSerializer, \
    CorporateOfficeSerializer, WarehouseSerializer, StorageSerializer, DockSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("id")
    serializer_class = TransactionSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by("id")
    serializer_class = OrganizationSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all().order_by("id")
    serializer_class = FacilitySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("id")
    serializer_class = ItemSerializer


class CorporateOfficeViewSet(viewsets.ModelViewSet):
    queryset = CorporateOffice.objects.all().order_by("id")
    serializer_class = CorporateOfficeSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by("id")
    serializer_class = WarehouseSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all().order_by("id")
    serializer_class = StorageSerializer


class DockViewSet(viewsets.ModelViewSet):
    queryset = Dock.objects.all().order_by("id")
    serializer_class = DockSerializer
