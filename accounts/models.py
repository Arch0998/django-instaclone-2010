from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from accounts.validators import custom_username_validator


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        help_text=_(
            "Required 30 characters or fewer. "
            "Letters, digits, dots and underscore only."
        ),
        validators=[custom_username_validator],
    )
    first_name = models.CharField(
        max_length=15,
    )
    last_name = models.CharField(
        max_length=15,
    )
    phone = models.CharField(
        max_length=18,
        unique=True,
        error_messages={
            "unique": _("A Phone number already exists."),
        },
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
        upload_to="media/avatars/",
        null=True,
        blank=True
    )
    profile_header = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return f"Profile: {self.user.username}"


class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following_set"
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followers_set"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("follower", "following")
