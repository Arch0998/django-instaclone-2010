from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import User, Follow


class TestUsersMixin:
    def setUp(self):
        self.user = User.objects.create(
            username="viewuser",
            first_name="Ivan",
            last_name="Ivanov",
            email="viewuser@example.com",
            phone="+380987654360"
        )
        self.user2 = User.objects.create(
            username="viewuser2",
            first_name="Petro",
            last_name="Petrov",
            email="viewuser2@example.com",
            phone="+380987654361"
        )


class IndexViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()

    def test_index_redirect_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("accounts:index"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.user.username, response.url)


class UserRegisterViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()

    def test_register(self):
        response = self.client.post(reverse("accounts:registration"), {
            "username": "newuser",
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "newuser@example.com",
            "phone": "+380987654362",
            "password1": "Testpass123!",
            "password2": "Testpass123!"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())


class UserProfileViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()

    def test_profile_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("accounts:profile", args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)


class ProfileEditViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)

    def test_get_edit_profile(self):
        response = self.client.get(reverse("accounts:edit_profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profile")

    def test_post_edit_profile(self):
        response = self.client.post(reverse("accounts:edit_profile"), {
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "editprofile@example.com",
            "phone": "+380987654363"
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, "editprofile@example.com")


class FollowUserViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)

    def test_follow_unfollow(self):
        url = reverse("accounts:follow", args=[self.user2.username])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Follow.objects.filter(
            follower=self.user, following=self.user2).exists())
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Follow.objects.filter(
            follower=self.user, following=self.user2).exists())


class FollowersListViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        Follow.objects.create(follower=self.user2, following=self.user)

    def test_followers_list(self):
        url = reverse("accounts:followers", args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user2.username)


class FollowingListViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        Follow.objects.create(follower=self.user, following=self.user2)

    def test_following_list(self):
        url = reverse("accounts:following", args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user2.username)


class SearchViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)

    def test_search(self):
        url = reverse("accounts:search") + "?q=viewuser2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user2.username)
