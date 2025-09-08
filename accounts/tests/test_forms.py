from django.test import TestCase

from accounts.forms import UserRegisterForm, UserEditForm, ProfileEditForm
from accounts.models import User


class TestUsersMixin:
    def setUp(self):
        self.user = User.objects.create(
            username="formuser",
            first_name="Ivan",
            last_name="Ivanov",
            email="formuser@example.com",
            phone="+380987654350"
        )
        self.user2 = User.objects.create(
            username="formuser2",
            first_name="Petro",
            last_name="Petrov",
            email="formuser2@example.com",
            phone="+380987654351"
        )


class UserRegisterFormTest(TestUsersMixin, TestCase):
    def test_valid_registration(self):
        form = UserRegisterForm(data={
            "username": "newuser",
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "newuser@example.com",
            "phone": "+380987654352",
            "password1": "Testpass123!",
            "password2": "Testpass123!"
        })
        self.assertTrue(form.is_valid())

    def test_duplicate_email(self):
        form = UserRegisterForm(data={
            "username": "anotheruser",
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "formuser@example.com",
            "phone": "+380987654353",
            "password1": "Testpass123!",
            "password2": "Testpass123!"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_duplicate_phone(self):
        form = UserRegisterForm(data={
            "username": "anotheruser",
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "another@example.com",
            "phone": "+380987654350",
            "password1": "Testpass123!",
            "password2": "Testpass123!"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors)


class UserEditFormTest(TestUsersMixin, TestCase):
    def test_valid_edit(self):
        form = UserEditForm(
            data={
                "first_name": "Ivan",
                "last_name": "Ivanov",
                "email": "edit@example.com",
                "phone": "+380987654354"
            },
            user=self.user
        )
        self.assertTrue(form.is_valid())

    def test_duplicate_email_edit(self):
        form = UserEditForm(
            data={
                "first_name": "Ivan",
                "last_name": "Ivanov",
                "email": "formuser2@example.com",
                "phone": "+380987654355"
            },
            user=self.user
        )
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_duplicate_phone_edit(self):
        form = UserEditForm(
            data={
                "first_name": "Ivan",
                "last_name": "Ivanov",
                "email": "edit2@example.com",
                "phone": "+380987654351"
            },
            user=self.user
        )
        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors)


class ProfileEditFormTest(TestUsersMixin, TestCase):
    def test_valid_profile_header(self):
        form = ProfileEditForm(
            data={"profile_header": "Hello world!"},
            instance=self.user.profile
        )
        self.assertTrue(form.is_valid())
