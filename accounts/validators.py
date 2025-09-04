from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


custom_username_validator = RegexValidator(
    regex=r'^[\w.]+$',
    message="Only letters, numbers, dot or underscore are allowed."
)


def validate_first_name(first_name):
    if not re.match(r'^[A-Za-zА-Яа-яЁёІіЇїЄє]{3,15}$', first_name):
        raise ValidationError(
            "First name must be 3-15 letters (no spaces, no digits)."
        )
    return first_name


def validate_last_name(last_name):
    if not re.match(r'^[A-Za-zА-Яа-яЁёІіЇїЄє]{3,15}$', last_name):
        raise ValidationError(
            "Last name must be 3-15 letters (no spaces, no digits)."
        )
    return last_name


def validate_phone(phone):
    if not re.match(r'^\+?\d{10,17}$', phone):
        raise ValidationError(
            "Phone must be digits, optionally starting with '+', 10-18 chars."
        )
    if phone.count('+') > 1 or (phone and '+' in phone[1:]):
        raise ValidationError("Only one '+' allowed and only at the start.")
    return phone


def validate_username(username):
    if len(username) < 3 or len(username) > 30:
        raise ValidationError("Username must be between 3 and 30 characters.")
    if not re.match(r'^[A-Za-z0-9._]+$', username):
        raise ValidationError(
            "Username can contain only letters, numbers, dot or underscore."
        )
    if username[0] in ['.', '_']:
        raise ValidationError("Username cannot start with dot or underscore.")
    if username.count('.') > 1 or username.count('_') > 1:
        raise ValidationError(
            "Username can contain only one dot OR one underscore."
        )
    if '.' in username and '_' in username:
        raise ValidationError(
            "Username can contain only one dot OR one underscore, not both."
        )
    return username
