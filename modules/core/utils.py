from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from enum import Enum


class DaysOfWeek(str, Enum):
    """"weekdays enum"""

    MON = "Monday"

    TUE = "Tuesday"

    WED = "Wednesday"

    THU = "Thursday"

    FRI = "Friday"

    SAT = "Saturday"

    SUN = "Sunday"

    @classmethod
    def choices(cls):
        return tuple((i.value, _(i.value.capitalize())) for i in cls)


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


class Validators:
    def validate_comma_separated_integer(value, test):
        if value.find('.') != 4:
            raise ValidationError(
                _('%(value)s decimal point incorrect (e.g. 1234.56)'),
                params={'value': value},
            )

    def zero_not_first_integer(value):
        form_input = str(value)
        if form_input[0] == '0':
            raise ValidationError(
                _('%(value)s first integer must not be zero'),
                params={'value': value}
            )

    def validate_working_hours_begin_end(value_start, value_end):
        if value_start > value_end:
            raise ValidationError(
                _('%(value_end) is before working hour starts'),
                params={'value': value_end},
            )
