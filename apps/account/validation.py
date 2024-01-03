from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class INNValidator(RegexValidator):
    regex = r'^\d{14}$'
    message = _("Enter a valid INN. This value may contain only 14 digits.")
    flags = 0
