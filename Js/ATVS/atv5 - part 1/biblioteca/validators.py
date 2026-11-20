from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_ano(value):
    if value < 1450 or value > timezone.now().year:
        raise ValidationError(
            'O ano deve ser valido: 1450-atual!'
        )

def validade_paginas(value):
    if value < 1 or value > 5000:
        raise ValidationError (
            'Numero de paginas deve ser valido: 1 - 5000!'
        )

def validade_isbn(value):
    if len(value) != 13:
        raise ValidationError (
            'O codigo do isbn deve ter 13 digitos!'
        )