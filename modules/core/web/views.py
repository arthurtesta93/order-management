from rest_framework import viewsets

from ..models.definitions import Organization, Facility, Item, CorporateOffice, Warehouse, Dock, Contact
from ..web.serializers import OrganizationSerializer, FacilitySerializer, ItemSerializer, \
    CorporateOfficeSerializer, WarehouseSerializer, DockSerializer, ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by("first_name")
    serializer_class = ContactSerializer


# view that filters contact by organization id

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


# viewset for searching facilities by zip code

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


# query purchase orders that contain a specific item, by item id

class CorporateOfficeViewSet(viewsets.ModelViewSet):
    queryset = CorporateOffice.objects.all().order_by("id")
    serializer_class = CorporateOfficeSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by("id")
    serializer_class = WarehouseSerializer


# view to filter warehouse by organization id

class WarehouseSearchByOrganizationViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by("id")
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        organization = self.request.query_params.get("organization", None)
        if organization is not None:
            return Warehouse.objects.filter(organization=organization)
        return Warehouse.objects.all()


class DockViewSet(viewsets.ModelViewSet):
    queryset = Dock.objects.all().order_by("id")
    serializer_class = DockSerializer


# view to filter dock by warehouse id

class DockSearchByWarehouseViewSet(viewsets.ModelViewSet):
    queryset = Dock.objects.all().order_by("id")
    serializer_class = DockSerializer

    def get_queryset(self):
        warehouse = self.request.query_params.get("warehouse", None)
        if warehouse is not None:
            return Dock.objects.filter(warehouse=warehouse)
        return Dock.objects.all()
