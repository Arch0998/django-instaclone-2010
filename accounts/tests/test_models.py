from django.test import TestCase
from django.db import IntegrityError

from accounts.models import User, UserProfile, Follow


class TestUsersMixin:
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            first_name="Ivan",
            last_name="Ivanov",
            phone="+380987654321"
        )
        self.user2 = User.objects.create(
            username="testuser2",
            first_name="Petro",
            last_name="Petrov",
            phone="+380987654322"
        )


class UserModelTest(TestUsersMixin, TestCase):
    def test_user_str(self):
        self.assertEqual(str(self.user), "testuser")

    def test_user_fields(self):
        self.assertEqual(self.user.first_name, "Ivan")
        self.assertEqual(self.user.last_name, "Ivanov")
        self.assertEqual(self.user.phone, "+380987654321")


class UserProfileModelTest(TestUsersMixin, TestCase):
    def test_profile_str(self):
        profile = self.user.profile
        self.assertEqual(str(profile), "Profile: testuser")

    def test_profile_header(self):
        profile = self.user.profile
        profile.profile_header = "Hello world!"
        profile.save()
        self.assertEqual(profile.profile_header, "Hello world!")

    def test_profile_user_relation(self):
        profile = self.user.profile
        self.assertEqual(profile.user, self.user)

    def test_profile_deleted_with_user(self):
        user_id = self.user.id
        self.user.delete()
        self.assertFalse(
            UserProfile.objects.filter(user_id=user_id).exists()
        )


class FollowModelTest(TestUsersMixin, TestCase):
    def test_follow_create(self):
        follow = Follow.objects.create(
            follower=self.user,
            following=self.user2
        )
        self.assertEqual(follow.follower, self.user)
        self.assertEqual(follow.following, self.user2)

    def test_follow_str(self):
        follow = Follow.objects.create(
            follower=self.user,
            following=self.user2
        )
        self.assertIn("testuser", str(follow))
        self.assertIn("testuser2", str(follow))

    def test_follow_user_relation(self):
        follow = Follow.objects.create(
            follower=self.user,
            following=self.user2
        )
        self.assertEqual(follow.follower, self.user)
        self.assertEqual(follow.following, self.user2)

    def test_follow_deleted_with_user(self):
        Follow.objects.create(
            follower=self.user,
            following=self.user2
        )
        user_id = self.user.id
        user2_id = self.user2.id
        self.user.delete()
        self.assertFalse(
            Follow.objects.filter(follower_id=user_id).exists()
        )
        self.user2.delete()
        self.assertFalse(
            Follow.objects.filter(following_id=user2_id).exists()
        )

    def test_follow_unique_constraint(self):
        Follow.objects.create(follower=self.user, following=self.user2)
        with self.assertRaises(IntegrityError):
            Follow.objects.create(follower=self.user, following=self.user2)

    def test_related_name_following_followers(self):
        follow = Follow.objects.create(
            follower=self.user,
            following=self.user2
        )
        self.assertIn(follow, self.user.following_set.all())
        self.assertIn(follow, self.user2.followers_set.all())
