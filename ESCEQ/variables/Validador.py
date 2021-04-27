from django.core.exceptions import ValidationError


def variables_validation(value):
    try:
        numerico = int(value)
    except:
        raise ValidationError('Dato debe ser numerico')
