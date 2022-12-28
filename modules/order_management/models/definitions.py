from decimal import Decimal

from django.db import models
from enum import Enum, unique

from modules.core.models.definitions import Transaction
from ..utils import Validators

# Create your models here.

"""Objective business-related entities / models"""


class ShippingOrder(Transaction):
    """A shipping order is a statement of intent, between a seller/buyer
     and a logistic provider, to move a one or more items. It contains many purchase orders """
    # TODO add organization selector

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


class PurchaseOrder(Transaction):
    """A purchase order is a transaction statement, between a buyer
     and a seller, for exchanged goods and services. It may belong to
     one or zero ShippingOrder. It may contain one or many Items """

    shipping_order_id = models.ForeignKey(ShippingOrder, on_delete=models.SET("N/A"))

    # TODO add params from serializer

    @property
    def total_items(self):
        total = Decimal("0")
        for item in self.items.all():
            total += item.total
        return total


# maybe Item should be an abstract definition for the general concept
# of an Item, and here we should have a OneToOne "ItemInstance" class with it's own ID

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
    count = models.CharField(validators=[Validators.zero_not_first_integer], max_length=7, default=0)
    package_type = models.CharField(max_length=2, choices=PACKAGE_TYPE)
    weight = models.IntegerField(validators=[Validators.validate_comma_separated_integer], default=0)
    weight_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT)
    height = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    width = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    length = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    dimension_unit = models.CharField(max_length=2, choices=DIMENSION_UNIT)

    def __str__(self):
        return f"{self.commodity} (purchase_order={self.purchase_order_id}, id={self.id})"

