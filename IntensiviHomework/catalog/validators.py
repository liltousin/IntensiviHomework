from functools import wraps

from django.core.exceptions import ValidationError


def validate_must_be_param(*words):
    @wraps(validate_must_be_param)
    def inner(value: str):
        for word in words:
            if word in value.lower():
                return value
        else:
            raise ValidationError(f'Нет {", ".join(words)}')

    return inner
