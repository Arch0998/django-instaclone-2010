from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password1",
            "password2"
        ]
