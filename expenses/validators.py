from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_dat_not_future(date):
    if date > timezone.now().date:
        raise ValidationError('Date cannot be in the future')