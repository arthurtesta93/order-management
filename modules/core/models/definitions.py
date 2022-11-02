from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum, unique

from ..models.abstractions import BaseModel

# Create your models here.

"""Higher level business-related abstractions"""


@unique
class TransactionalKind(str, Enum):
    """Defines the transaction type"""

    ORDER = "ORDER"
    ITEM = "ITEM"

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
        default=TransactionalKind.ORDER.value,
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

    def __str__(self):
        return f"{self.name} (kind={self.kind}, id={self.id})"
