from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum, unique

from ..utils import CountryList

from ..models.abstractions import BaseModel

# Create your models here.
from ...order_management.utils import Validators

"""Higher level business-related abstractions"""


@unique
class TransactionalKind(str, Enum):
    """Defines the transaction type"""

    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

    @classmethod
    def choices(cls):
        return tuple((i.value, _(i.name.capitalize())) for i in cls)


class Transaction(BaseModel):
    """Represents anything that can be transmitted as a logistic service request"""

    # name = models.CharField(max_length=1024, verbose_name="Name")
    kind = models.CharField(
        max_length=1024,
        choices=TransactionalKind.choices(),
        null=False,
        blank=True,
        default=TransactionalKind.OUTBOUND.value,
        verbose_name=_("Kind"),
    )

    def __str__(self):
        return f"(kind={self.kind}, id={self.id})"


class OrganizationKind(str, Enum):
    """Defines the role of an organization in the logistic process"""

    SELLER = "SELLER"

    BUYER = "BUYER"

    SHIPPER = "SHIPPER"

    CONSIGNEE = "CONSIGNEE"

    CARRIER = "CARRIER"

    TRANSPORT_MANAGER = "TRANSPORT_MANAGER"

    UNDEFINED = "UNDEFINED"

    @classmethod
    def choices(cls):
        return tuple((i.value, _(i.name.capitalize())) for i in cls)


class Organization(BaseModel):
    """Represents a person or entity that will be part of any business operation"""

    name = models.CharField(max_length=1024, verbose_name="Name")
    kind = models.CharField(
        max_length=1024,
        choices=OrganizationKind.choices(),
        null=False,
        blank=True,
        default=OrganizationKind.UNDEFINED.value,
        verbose_name=_("Kind"),
    )
    external_contact_name = models.CharField(max_length=120, verbose_name="Contact Name", default=None)  # TODO Create specific model w/ contact information
    external_contact_phone = models.CharField
    internal_contact_name = models.CharField(max_length=120,
                                             verbose_name="Account Manager", default=None)  # TODO Create specific model

    def __str__(self):
        return f"{self.name} (kind={self.kind}, id={self.id})"


class Item(BaseModel):
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

    part_number = models.CharField(max_length=50, null=True, default=None)
    commodity = models.CharField(max_length=128)
    count = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    package_type = models.CharField(max_length=2, choices=PACKAGE_TYPE)
    weight_package_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT)
    height_package_unit = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    width_package_unit = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    length_package_unit = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    dimension_unit = models.CharField(max_length=2, choices=DIMENSION_UNIT)
    hazardous = models.BooleanField(default=False)
    temperature_controlled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.commodity} PN#{self.part_number}"


class Facility(BaseModel):
    """A facility represents a physical space belonging
        to one and only one organization to serve specific purposes"""
    class Meta:
        verbose_name_plural = "facilities"

    organization = models.ForeignKey(Organization, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, default=None)
    zip_code = models.CharField(max_length=10, null=True, default=None)
    street = models.CharField(max_length=50, null=True, default=None)
    street_number = models.IntegerField(default=0)
    city = models.CharField(max_length=20, null=True, default=None)
    state = models.CharField(max_length=20, null=True, default=None)
    country = models.CharField(max_length=20, choices=CountryList.choices())
