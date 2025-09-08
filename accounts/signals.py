from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from functools import wraps

from accounts.models import UserProfile


def disable_for_loaddata(signal_handler):
    """
    Decorator that turns off signal handlers when loading fixture data.
    """
    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        if kwargs.get("raw"):
            return
        signal_handler(*args, **kwargs)
    return wrapper


@disable_for_loaddata
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@disable_for_loaddata
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()
    else:
        UserProfile.objects.create(user=instance)
