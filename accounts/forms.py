from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.models import User, UserProfile


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "A user with this email already exists."
            )
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if User.objects.filter(phone=phone).exists():
            raise ValidationError(
                "A user with this phone number already exists."
            )
        return phone


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if (
            User.objects.filter(email=email)
            .exclude(id=self.user.id if self.user else None)
            .exists()
        ):
            raise ValidationError(
                "A user with this email already exists."
            )
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if (
            User.objects.filter(phone=phone)
            .exclude(id=self.user.id if self.user else None)
            .exists()
        ):
            raise ValidationError(
                "A user with this phone number already exists."
            )
        return phone


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar", "profile_header"]
        widgets = {
            "profile_header": forms.TextInput(
                attrs={
                    "placeholder": "Tell people about yourself...",
                    "maxlength": "50",
                }
            )
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if avatar:
            if avatar.size > 5 * 1024 * 1024:
                raise ValidationError(
                    "Avatar file size should not exceed 5MB."
                )

            allowed_extensions = [".jpg", ".jpeg", ".png"]
            file_extension = avatar.name.lower().split(".")[-1]
            if f".{file_extension}" not in allowed_extensions:
                raise ValidationError(
                    "Only JPG, JPEG and PNG files are allowed."
                )

        return avatar
