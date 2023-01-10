from django.utils.translation import gettext_lazy as _

from enum import Enum


class CountryList(str, Enum):
    """Defines the role of an organization in the logistic process"""

    USA = "UNITED STATES"

    BRA = "BRAZIL"

    ARG = "ARGENTINA"

    CAN = "CANADA"

    MEX = "MEXICO"

    GBR = "GREAT BRITAIN"

    URU = "URUGUAY"

    @classmethod
    def choices(cls):
        return tuple((i.value, _(i.value.capitalize())) for i in cls)
