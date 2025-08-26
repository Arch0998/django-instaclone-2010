from django.core.validators import RegexValidator


custom_username_validator = RegexValidator(
    regex=r'^[\w.]+$',
    message="Only letters, numbers, dots and underscores are allowed."
)
