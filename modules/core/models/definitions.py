from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib import admin

from enum import Enum

from ..utils import CountryList, Validators, default_days_week

from ..models.abstractions import BaseModel

# Create your models here.

"""Higher level business-related abstractions"""


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
    yearly_revenue = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


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
    weight = models.CharField(max_length=3)
    height_package_unit = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    width_package_unit = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    length_package_unit = models.IntegerField(validators=[Validators.zero_not_first_integer], default=0)
    dimension_unit = models.CharField(max_length=2, choices=DIMENSION_UNIT)
    hazardous = models.BooleanField(default=False)
    temperature_controlled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.commodity} PN#{self.part_number}"


class Contact(BaseModel):
    """"Base model for contacts"""

    first_name = models.CharField(default=None, max_length=30, verbose_name="First Name")
    last_name = models.CharField(default=None, max_length=30, verbose_name="Last Name")
    email = models.EmailField(default=None, max_length=40, verbose_name="Email")
    phone = models.CharField(default=None, max_length=20, verbose_name="Phone")
    observations = models.CharField(blank=True, null=True, default=None, max_length=128)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL, default=None)

    @admin.display(ordering='organization__name', description='Organization')
    def get_organization(self):
        return self.organization.name


class Facility(BaseModel):
    """A facility represents a physical space belonging
        to one and only one organization to serve specific purposes"""

    class Meta:
        verbose_name_plural = "facilities"

    working_days = models.JSONField(default=default_days_week)

    working_hour_start = models.TimeField(auto_now_add=False, default=None, null=True, blank=True)
    working_hour_end = models.TimeField(auto_now_add=False, default=None, null=True, blank=True)  # TODO validation

    name = models.CharField(max_length=50, null=True, default=None)
    organization = models.ForeignKey(Organization, related_name="+", on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10, null=True, default=None)
    street = models.CharField(max_length=50, null=True, default=None)
    street_number = models.IntegerField(default=0)
    city = models.CharField(max_length=20, null=True, default=None)
    state = models.CharField(max_length=20, null=True, default=None)
    country = models.CharField(max_length=20, choices=CountryList.choices())
    observations = models.CharField(blank=True, null=True, default=None, max_length=128)

    label = models.CharField(blank=True, null=True, default=None, max_length=10)

    refrigerated_storage = models.BooleanField(default=False)
    drop_trailer = models.BooleanField(default=False)

    dispatch_contact = models.ForeignKey(Contact, related_name="+", on_delete=models.DO_NOTHING,
                                         default=None)
    contact = models.ForeignKey(Contact, null=True, related_name="+", on_delete=models.DO_NOTHING, default=None)

    def get_contact_number(self):
        return self.contact.phone
    @admin.display(ordering='contact__name', description='Contact')
    def get_contact(self):
        return self.contact.first_name

    @admin.display(ordering='contact__email', description='Email')
    def get_contact_email(self):
        return self.contact.email


class CorporateOffice(Facility):
    class Meta:
        verbose_name = "Corporate Office"
        verbose_name_plural = "Corporate Offices"

    billable = models.BooleanField(default=True)
    # add billing related fields


class Warehouse(Facility):

    free_reschedule_enabled = models.BooleanField(default=True)
    allow_repackaging_until_appointment = models.BooleanField(default=True)
    time_allowed_for_repackaging_before_appointment = models.TimeField(auto_now_add=False, default=None, null=True,
                                                                       blank=True)
    detention_daily_cost = models.IntegerField(default=0)
    warehouse_label = models.CharField(max_length=10, null=True, default=None)

    @admin.display(ordering='dispatch_contact__name', description='Dispatch Contact')
    def get_dispatch_contact(self):
        return self.dispatch_contact.first_name + " " + self.dispatch_contact.last_name

class Dock(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name="Warehouse", on_delete=models.DO_NOTHING, default=None)
    dock_dispatch_contact = models.ForeignKey(Contact, related_name="+", on_delete=models.DO_NOTHING,
                                              default=None, null=True, blank=True)
    refrigerated_cargo = models.BooleanField(default=False)
    drop_trailer = models.BooleanField(default=False)
    drayage_enabled = models.BooleanField(default=False)
    live_load = models.BooleanField(default=True)
    hazmat = models.BooleanField(default=False)
    lumper_required = models.BooleanField(default=False)
    appointment_slot_time_hours = models.FloatField(default=0)
    dock_label = models.CharField(max_length=10, null=True, default=None)