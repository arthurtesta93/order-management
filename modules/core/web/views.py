from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.definitions import Organization, Facility, Item, CorporateOffice, Warehouse, Dock, Contact
from ..web.serializers import OrganizationSerializer, FacilitySerializer, ItemSerializer, \
    CorporateOfficeSerializer, WarehouseSerializer, DockSerializer, ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by("first_name")
    serializer_class = ContactSerializer


# view that filters contact by organization id


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by("id")
    serializer_class = OrganizationSerializer

    @action(detail=False, methods=['GET'])
    def filter_by_name(self, request):
        name = request.query_params.get('name')
        organizations = Organization.objects.filter(name=name)
        serializer = self.get_serializer(organizations, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def filter_by_kind(self, request):
        kind = request.query_params.get('kind')
        organizations = Organization.objects.filter(kind=kind)
        serializer = self.get_serializer(organizations, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def filter_by_yearly_revenue(self, request):
        yearly_revenue = request.query_params.get('yearly_revenue')
        organizations = Organization.objects.filter(yearly_revenue=yearly_revenue)
        serializer = self.get_serializer(organizations, many=True)
        return Response(serializer.data)


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all().order_by("id")
    serializer_class = FacilitySerializer

    @action(detail=False, methods=['GET'])
    def filter_by_zip_code(self, request, ):
        zip_code = request.query_params.get('zip_code')
        print(f"Filtering by zip code: {zip_code}")
        facilities = Facility.objects.filter(zip_code=zip_code)
        serializer = self.get_serializer(facilities, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def filter_by_organization(self, request):
        organization_id = request.query_params.get('organization_id')
        facilities = Facility.objects.filter(organization_id=organization_id)
        serializer = self.get_serializer(facilities, many=True)
        return Response(serializer.data)


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


class DockViewSet(viewsets.ModelViewSet):
    queryset = Dock.objects.all().order_by("id")
    serializer_class = DockSerializer
