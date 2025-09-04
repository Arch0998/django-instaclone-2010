from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts import views


class AccountsUrlsTest(SimpleTestCase):
    def test_index_url(self):
        url = reverse("accounts:index")
        self.assertEqual(
            resolve(url).func.view_class, views.IndexView
        )

    def test_logout_url(self):
        url = reverse("accounts:logout")
        self.assertEqual(
            resolve(url).func.view_class.__name__, "LogoutView"
        )

    def test_registration_url(self):
        url = reverse("accounts:registration")
        self.assertEqual(
            resolve(url).func.view_class, views.UserRegisterView
        )

    def test_edit_profile_url(self):
        url = reverse("accounts:edit_profile")
        self.assertEqual(
            resolve(url).func.view_class, views.ProfileEditView
        )

    def test_search_url(self):
        url = reverse("accounts:search")
        self.assertEqual(
            resolve(url).func.view_class, views.SearchView
        )

    def test_profile_url(self):
        url = reverse("accounts:profile", args=["testuser"])
        self.assertEqual(
            resolve(url).func.view_class, views.UserProfileView
        )

    def test_follow_url(self):
        url = reverse("accounts:follow", args=["testuser"])
        self.assertEqual(
            resolve(url).func.view_class, views.FollowUserView
        )

    def test_followers_url(self):
        url = reverse("accounts:followers", args=["testuser"])
        self.assertEqual(
            resolve(url).func.view_class, views.FollowersListView
        )

    def test_following_url(self):
        url = reverse("accounts:following", args=["testuser"])
        self.assertEqual(
            resolve(url).func.view_class, views.FollowingListView
        )
