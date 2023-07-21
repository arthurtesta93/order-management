import syslog
from decimal import Decimal
from enum import Enum

from django.db import models
from django.contrib import admin

from modules.order_management.models.abstractions import BaseModel
from modules.core.models.definitions import Organization, Facility, Item

# Create your models here.

"""Objective business-related entities / models"""


class Transaction(BaseModel):
    """Represents anything that can be transmitted as a logistic service request"""

    TRANSACTION_KIND = (
        ('INBOUND', 'Inbound'),
        ('OUTBOUND', 'Outbound')
    )

    # name = models.CharField(max_length=1024, verbose_name="Name")
    kind = models.CharField(
        max_length=1024,
        choices=TRANSACTION_KIND,
        null=False,
        blank=True,
        default='OUTBOUND',
        verbose_name="Kind",
    )

    def __str__(self):
        return f"(kind={self.kind}, id={self.id})"


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
    customer_reference = models.CharField(max_length=128, default='')
    carrier = models.ForeignKey(Organization, null=True, default=None, related_name="carrier",
                                on_delete=models.SET_NULL)
    bill_to = models.ForeignKey(Organization, null=True, default=None, related_name="+", on_delete=models.SET_NULL)
    ship_from = models.ForeignKey(Facility, null=True, default=None, related_name="+", on_delete=models.SET_NULL)
    ship_to = models.ForeignKey(Facility, null=True, default=None, related_name="+", on_delete=models.SET_NULL)
    shipping_order_status = models.CharField(choices=SHIPPING_ORDER_STATUS, null=False, default='EMPTY', max_length=14)

    def __str__(self):
        return f"SO#{self.id} : {self.shipping_order_status}"

    @admin.display(ordering='facility__name', description='Ship From')
    def get_ship_from(self):
        return self.ship_from.name

    @admin.display(ordering='facility__name', description='Ship To')
    def get_ship_to(self):
        return self.ship_to.name

#    def ship_from(self):
#        return f"{self.ship_from}"
#    def pickup_date(self):
 #       return self.model._default_manager.get_queryset()



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

    def __str__(self):
        return f"PO#{self.id} : {self.purchase_order_status}"


class ItemInstance(BaseModel):
    """Produced Item abstraction, attributed to a specific purchase order by a seller to be acquired by a buyer"""
    item = models.ForeignKey(Item, related_name="item", on_delete=models.SET("N/A"))
    quantity = models.IntegerField()
    purchase_order_id = models.ForeignKey(PurchaseOrder, related_name="purchase-order+", on_delete=models.SET("N/A"))
    special_instructions = models.CharField(max_length=128, null=True, default=None)

    def __str__(self):
        return f"#{self.id} {self.item.commodity} {self.purchase_order_id}"
