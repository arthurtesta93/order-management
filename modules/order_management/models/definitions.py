from decimal import Decimal

from django.db import models

from modules.core.models.definitions import Transaction, Organization, Item

# Create your models here.

"""Objective business-related entities / models"""


class ShippingOrder(Transaction):
    """A shipping order is a statement of intent, between a seller/buyer
     and a logistic provider, to move a one or more items. It contains many purchase orders """
    # TODO add organizations selector (facility from, facility to, carrier (nullable)

    TRANSPORT_TYPE = (
        ('TL', 'Truck Load'),
        ('LTL', 'Less than Truck Load'),
        ('PTL', 'Partial Truck Load'),
        ('RAIL', 'Rail'),
        ('DRAYAGE', 'Drayage')
    )

    mode = models.CharField(choices=TRANSPORT_TYPE, null=True, default=None, max_length=7)
    date_received = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateTimeField(auto_now_add=False)
    delivery_date = models.DateTimeField(auto_now_add=False)
    reference = models.CharField(max_length=128, default='')

#    ship_from = models.ForeignKey()
#    ship_to = models.ForeignKey()

#   bill_to = models.ForeignKey()


class PurchaseOrder(Transaction):
    """A purchase order is a transaction statement, between a buyer
     and a seller, for exchanged goods and services. It may belong to
     one or zero ShippingOrder. It may contain one or many Items """

    shipping_order_id = models.ForeignKey(ShippingOrder, on_delete=models.SET("N/A"))
    # TODO add params from serializer
    # buyer / seller

    @property
    def total_items(self):
        total = Decimal("0")
        for item in self.items.all():
            total += item.total
        return total


class ItemInstance(Item):
    purchase_order_id = models.ForeignKey(PurchaseOrder, related_name="items", on_delete=models.SET("N/A"))
    serial_number = models.CharField(max_length=50, null=True, default=None)
    special_instructions = models.CharField(max_length=128, null=True, default=None)


