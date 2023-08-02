from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



def default_days_week():
    return dict(
        [
            (day, False)
            for day in [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        ]
    )



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
