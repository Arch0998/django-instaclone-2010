from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


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
