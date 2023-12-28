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

    SHIPPING_ORDER_STATUS = (
        ('EMPTY', 'Empty'),
        ('PROCESSED', 'Processed'),
        ('AWARDED', 'Awarded'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('POD_CONFIRMED', 'Proof Of Delivery Confirmed'),
        ('INVOICED', 'Invoiced')
    )

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

    @classmethod
    def create(cls, *args, **kwargs):
        """Create a new ShippingOrder instance"""
        shipping_order = cls(*args, **kwargs)
        shipping_order.save()
        return shipping_order

    def __str__(self):
        return f"SO#{self.id} : {self.shipping_order_status}"

    @admin.display(ordering='facility__name', description='Ship From')
    def get_ship_from(self):
        return self.ship_from.name

    @admin.display(ordering='facility__name', description='Ship To')
    def get_ship_to(self):
        return self.ship_to.name

    def update_shipping_order_status(self, status):
        self.shipping_order_status = status
        self.save()


class PurchaseOrder(Transaction):
    """A purchase order is a transaction statement, between a buyer
     and a seller, for exchanged goods and services. It may belong to
     one or zero ShippingOrder. It may contain one or many Items """

    PURCHASE_ORDER_STATUS = (
        ('PLANNED', 'Planned'),
        ('PROCESSED', 'Processed'),
        ('PACKED', 'Packed'),
        ('PLACED', 'Placed'),
    )

    shipping_order_id = models.ForeignKey(ShippingOrder, on_delete=models.SET("N/A"))
    buyer = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL, related_name="buyer")
    seller = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL, related_name="seller")
    purchase_order_status = models.CharField(choices=PURCHASE_ORDER_STATUS, null=False, default='PLANNED', max_length=9)

    def __str__(self):
        return f"PO#{self.id} : {self.purchase_order_status}"

    # TODO - we are accessing the shipping order status here, but we should be calling a function on the shipping order
    def check_shipping_order_status(self) -> None:
        syslog.syslog(syslog.LOG_INFO, f"Shipping order status: {self.shipping_order_id.shipping_order_status}")
        if self.shipping_order_id.shipping_order_status == 'EMPTY':
            self.shipping_order_id.shipping_order_status = 'PROCESSED'
            self.shipping_order_id.save()

    def save(self, *args, **kwargs):
        self.check_shipping_order_status()
        super(PurchaseOrder, self).save(*args, **kwargs)

    @admin.display(ordering='buyer__id', description='Buyer')
    def get_buyer(self):
        return self.buyer.name

    @admin.display(ordering='seller_id', description='Seller')
    def get_seller(self):
        return self.seller.name

    def update_order_status(self, status):
        print(f"Updating purchase order status to {status}")

        if status in [x[0] for x in self.PURCHASE_ORDER_STATUS]:
            self.purchase_order_status = status
            self.save()
        else:
            raise ValueError(
                f"Invalid purchase order status: {status}. Must be one of {PurchaseOrder.PURCHASE_ORDER_STATUS}")


class ItemInstance(BaseModel):
    """Produced Item abstraction, attributed to a specific purchase order by a seller to be acquired by a buyer"""
    item = models.ForeignKey(Item, related_name="item", on_delete=models.SET("N/A"))
    quantity = models.IntegerField()
    purchase_order_id = models.ForeignKey(PurchaseOrder, related_name="purchase-order+", on_delete=models.SET("N/A"))
    special_instructions = models.CharField(max_length=128, null=True, default=None, blank=True)

    def __str__(self):
        return f"# {self.item.commodity} {self.id} {self.purchase_order_id}"

    # TODO - we are accessing the purchase order status here, but we should be calling a function on the purchase order
    def check_purchase_order_status(self):
        syslog.syslog(syslog.LOG_INFO, f"Purchase order status: {self.purchase_order_id.purchase_order_status}")
        if self.purchase_order_id.purchase_order_status == 'PLANNED':
            self.purchase_order_id.purchase_order_status = 'PRODUCED'
            self.purchase_order_id.save()

    def save(self, *args, **kwargs):
        self.check_purchase_order_status()
        super(ItemInstance, self).save(*args, **kwargs)

    @admin.display(ordering='item__commodity', description='Item')
    def get_commodity(self):
        return self.item.commodity
