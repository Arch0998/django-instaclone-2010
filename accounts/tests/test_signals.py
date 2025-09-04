from django.test import TestCase

from accounts.models import User, UserProfile


class TestUsersMixin:
    def setUp(self):
        self.user = User.objects.create(username="signaluser")


class UserProfileSignalTest(TestUsersMixin, TestCase):
    def test_profile_created_on_user_creation(self):
        self.assertTrue(
            UserProfile.objects.filter(user=self.user).exists()
        )

    def test_profile_not_created_on_loaddata(self):
        from accounts.signals import create_user_profile
        create_user_profile(
            sender=User,
            instance=self.user,
            created=True,
            raw=True
        )
        profiles = UserProfile.objects.filter(user=self.user)
        self.assertEqual(profiles.count(), 1)
