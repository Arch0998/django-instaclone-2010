from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(
        max_length=18,
        unique=True
    )

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Profile: {self.user.username}"
