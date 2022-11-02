from decimal import Decimal

from django.db import models
from enum import Enum, unique

from modules.core.models.definitions import Transaction

# Create your models here.

"""Objective business-related entities / models"""


@unique
class OrderKind(str, Enum):
    """Types of shipping order"""

    LTL = "LTL"
    FTL = "FTL"

    @classmethod
    def choices(cls):
        return tuple((i.value, (i.name.capitalize())) for i in cls)


class ShippingOrder(Transaction):
    """A shipping order is a statement of intent, between a seller/buyer
     and a logistic provider, to move a one or more items. It contains many purchase orders """

    mode = OrderKind.choices()
    date_received = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=True)


class PurchaseOrder(Transaction):
    """A purchase order is a transaction statement, between a buyer
     and a seller, for exchanged goods and services. It may belong to
     one or zero ShippingOrder. It may contain one or many Items """

    shipping_order_id = models.ForeignKey(ShippingOrder, related_name="items", on_delete=models.SET("N/A"))

    @property
    def total_items(self):
        total = Decimal("0")
        for item in self.items.all():
            total += item.total
        return total


class Item(models.Model):
    """An Item represents a package of a specific commodity to be transported within
        a purchase order. It must belong to one and only one purchase order. """

    PACKAGE_TYPE = (
        ('PL', 'Pallet'),
        ('BX', 'Box'),
        ('BU', 'Bulk'),
    )
    WEIGHT_UNIT = (
        ('LB', 'POUNDS'),
        ('KG', 'KILOGRAMS'),
        ('OZ', 'OUNCE')
    )
    DIMENSION_UNIT = (
        ('IN', 'INCHES'),
        ('FT', 'FEET'),
        ('YD', 'YARD'),
        ('MT', 'METER'),
        ('CM', 'CENTIMETER')
    )

    purchase_order_id = models.ForeignKey(PurchaseOrder, related_name="items", on_delete=models.SET("N/A"))
    commodity = models.CharField(max_length=128)
    count = models.IntegerField
    package_type = models.CharField(max_length=2, choices=PACKAGE_TYPE)
    weight = models.IntegerField
    weight_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT)
    height = models.IntegerField
    width = models.IntegerField
    length = models.IntegerField
    dimension_unit = models.CharField(max_length=2, choices=DIMENSION_UNIT)
