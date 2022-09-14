from django.shortcuts import render

from rest_framework import viewsets

from ..models.definitions import Transaction, Organization
from ..web.serializers import TransactionSerializer, OrganizationSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("id")
    serializer_class = TransactionSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by("id")
    serializer_class = OrganizationSerializer
