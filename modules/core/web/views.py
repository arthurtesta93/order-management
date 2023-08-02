from django.shortcuts import render

from rest_framework import viewsets

from ..models.definitions import Organization, Facility, Item, CorporateOffice, Warehouse, Dock, Contact
from ..web.serializers import OrganizationSerializer, FacilitySerializer, ItemSerializer, \
    CorporateOfficeSerializer, WarehouseSerializer, DockSerializer, ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by("first_name")
    serializer_class = ContactSerializer


class ContactSearchViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by("first_name")
    serializer_class = ContactSerializer

    def get_queryset(self):
        first_name = self.request.query_params.get("first_name", None)
        if first_name is not None:
            return Contact.objects.filter(first_name=first_name)
        return Contact.objects.all()


class ContactSearchByOrganizationViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by("first_name")
    serializer_class = ContactSerializer

    def get_queryset(self):
        organization = self.request.query_params.get("organization", None)
        if organization is not None:
            return Contact.objects.filter(organization=organization)
        return Contact.objects.all()


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by("id")
    serializer_class = OrganizationSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all().order_by("id")
    serializer_class = FacilitySerializer


class FacilitySearchByOrganizationViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all().order_by("id")
    serializer_class = FacilitySerializer

    def get_queryset(self):
        organization = self.request.query_params.get("organization", None)
        if organization is not None:
            return Facility.objects.filter(organization=organization)
        return Facility.objects.all()


class FacilitySearchByZipCodeViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all().order_by("id")
    serializer_class = FacilitySerializer

    def get_queryset(self):
        zip_code = self.request.query_params.get("zip_code", None)
        if zip_code is not None:
            return Facility.objects.filter(zip_code=zip_code)
        return Facility.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("id")
    serializer_class = ItemSerializer


class CorporateOfficeViewSet(viewsets.ModelViewSet):
    queryset = CorporateOffice.objects.all().order_by("id")
    serializer_class = CorporateOfficeSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by("id")
    serializer_class = WarehouseSerializer


class DockViewSet(viewsets.ModelViewSet):
    queryset = Dock.objects.all().order_by("id")
    serializer_class = DockSerializer


class DockSearchByWarehouseViewSet(viewsets.ModelViewSet):
    queryset = Dock.objects.all().order_by("id")
    serializer_class = DockSerializer

    def get_queryset(self):
        warehouse = self.request.query_params.get("warehouse", None)
        if warehouse is not None:
            return Dock.objects.filter(warehouse=warehouse)
        return Dock.objects.all()


