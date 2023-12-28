from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from ..models.definitions import ShippingOrder, PurchaseOrder, ItemInstance, Transaction
from ..web.serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer, ShippingOrderSerializer, \
    TransactionSerializer
from ..web.services import process_purchase_order


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("id")
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['post'])
    def delete(self, request, pk=None):
        transaction = self.get_object()
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    @action(detail=True, methods=['post'])
    def process_order(self, request, pk=None):
        print(f"Processing order with id: {pk}")
        try:
            # Call your service function
            process_purchase_order(pk)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'PurchaseOrder not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class PurchaseOrderItemsViewSet(viewsets.ModelViewSet):
    queryset = ItemInstance.objects.all().order_by("id")
    serializer_class = PurchaseOrderItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemInstance.objects.all().order_by("id")
    serializer_class = PurchaseOrderItemSerializer
