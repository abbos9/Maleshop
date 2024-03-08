from django.core.exceptions import ValidationError


def rating_value_validator(value):
    if not 1 <= value <=5:
        raise ValidationError(
            value("Value Error !"),
            params={'value': value},
            )