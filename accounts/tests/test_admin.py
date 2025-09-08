from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from accounts.models import User, UserProfile, Follow
from accounts.admin import UserAdmin, UserProfileAdmin, FollowAdmin


class TestUsersMixin:
    def setUp(self):
        self.user = User.objects.create(
            username="adminuser",
            phone="+380987654340"
        )
        self.user2 = User.objects.create(
            username="adminuser2",
            phone="+380987654341"
        )


class MockRequest:
    pass


class UserAdminTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.admin = UserAdmin(User, self.site)

    def test_list_display(self):
        self.assertIn("username", self.admin.list_display)
        self.assertIn("phone", self.admin.list_display)

    def test_search_fields(self):
        self.assertIn("username", self.admin.search_fields)
        self.assertIn("phone", self.admin.search_fields)


class UserProfileAdminTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.profile = self.user.profile
        self.admin = UserProfileAdmin(UserProfile, self.site)

    def test_list_display(self):
        self.assertIn("user", self.admin.list_display)
        self.assertIn("avatar", self.admin.list_display)

    def test_search_fields(self):
        self.assertIn("user__username", self.admin.search_fields)


class FollowAdminTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.follow = Follow.objects.create(
            follower=self.user,
            following=self.user2
        )
        self.admin = FollowAdmin(Follow, self.site)

    def test_list_display(self):
        self.assertIn("follower", self.admin.list_display)
        self.assertIn("following", self.admin.list_display)

    def test_search_fields(self):
        self.assertIn("follower__username", self.admin.search_fields)
        self.assertIn("following__username", self.admin.search_fields)
