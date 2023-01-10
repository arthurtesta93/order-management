from django.shortcuts import render

from rest_framework import viewsets

from ..models.definitions import Transaction, Organization, Facility
from ..web.serializers import TransactionSerializer, OrganizationSerializer, FacilitySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("id")
    serializer_class = TransactionSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by("id")
    serializer_class = OrganizationSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all().order_by("id")
    serializer_class = FacilitySerializer
