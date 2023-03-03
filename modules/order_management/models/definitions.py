import syslog
from decimal import Decimal

from django.db import models

from modules.core.models.definitions import Transaction, Organization, Item, Storage, CorporateOffice, Warehouse, \
    Facility

# Create your models here.

"""Objective business-related entities / models"""


class ShippingOrder(Transaction):
    """A shipping order is a statement of intent, between a seller/buyer
     and a logistic provider, to move a one or more items. It contains many purchase orders """

    TRANSPORT_TYPE = (
        ('TL', 'Truck Load'),
        ('LTL', 'Less than Truck Load'),
        ('PTL', 'Partial Truck Load'),
        ('RAIL', 'Rail'),
        ('DRAYAGE', 'Drayage')
    )

    FACILITY_TYPE = (
        ('STORAGE', 'Storage'),
        ('CORPORATE', 'Corporate Office'),
        ('WAREHOUSE', 'Warehouse'),
        ('FACILITY', 'Facility'),  # Generic
    )

    SHIPPING_ORDER_STATUS = (
        ('EMPTY', 'Empty'),
        ('PROCESSED', 'Processed'),
        ('AWARDED', 'Awarded'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('POD_CONFIRMED', 'Proof Of Delivery Confirmed'),
        ('INVOICED', 'Invoiced')
    )

    facility_type = models.CharField(choices=FACILITY_TYPE, null=False, default='WAREHOUSE', max_length=10)

    mode = models.CharField(choices=TRANSPORT_TYPE, null=True, default=None, max_length=7)
    date_received = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateTimeField(auto_now_add=False)
    delivery_date = models.DateTimeField(auto_now_add=False)
    reference = models.CharField(max_length=128, default='')
    carrier = models.ForeignKey(Organization, null=True, default=None, related_name="carrier",
                                on_delete=models.SET_NULL)
    bill_to = models.ForeignKey(Organization, null=True, default=None, related_name="+", on_delete=models.SET_NULL)
    ship_from = models.ForeignKey(Facility, null=True, default=None, related_name="+", on_delete=models.SET_NULL)
    ship_to = models.ForeignKey(Facility, null=True, default=None, related_name="+", on_delete=models.SET_NULL)
    shipping_order_status = models.CharField(choices=SHIPPING_ORDER_STATUS, null=False, default='EMPTY', max_length=14)


class PurchaseOrder(Transaction):
    """A purchase order is a transaction statement, between a buyer
     and a seller, for exchanged goods and services. It may belong to
     one or zero ShippingOrder. It may contain one or many Items """

    PURCHASE_ORDER_STATUS = (
        ('PLANNED', 'Planned'),
        ('PRODUCED', 'Processing'),
        ('PICKED', 'Packed'),
        ('PLACED', 'Placed'),
    )

    shipping_order_id = models.ForeignKey(ShippingOrder, on_delete=models.SET("N/A"))
    buyer = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL, related_name="buyer")
    seller = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL, related_name="seller")
    purchase_order_status = models.CharField(choices=PURCHASE_ORDER_STATUS, null=False, default='PLANNED', max_length=9)


    @property
    def total_items(self):
        total = Decimal("0")
        for item in self.items.all():
            total += item.total
        return total


class ItemInstance(Item):
    """Produced Item abstraction, attributed to a specific purchase order by a seller to be acquired by a buyer"""

    purchase_order_id = models.ForeignKey(PurchaseOrder, related_name="items", on_delete=models.SET("N/A"))
    serial_number = models.CharField(max_length=50, null=True, default=None)
    special_instructions = models.CharField(max_length=128, null=True, default=None)
