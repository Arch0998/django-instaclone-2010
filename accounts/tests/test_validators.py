from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.validators import (
    validate_first_name,
    validate_last_name,
    validate_phone,
    validate_username
)


class TestValidators(TestCase):
    def test_valid_first_name(self):
        self.assertEqual(validate_first_name("Іван"), "Іван")
        self.assertEqual(validate_first_name("John"), "John")

    def test_invalid_first_name(self):
        with self.assertRaises(ValidationError):
            validate_first_name("Iv")
        with self.assertRaises(ValidationError):
            validate_first_name("Iv@n")
        with self.assertRaises(ValidationError):
            validate_first_name("Iv123")

    def test_valid_last_name(self):
        self.assertEqual(validate_last_name("Петров"), "Петров")
        self.assertEqual(validate_last_name("Smith"), "Smith")

    def test_invalid_last_name(self):
        with self.assertRaises(ValidationError):
            validate_last_name("Sm")
        with self.assertRaises(ValidationError):
            validate_last_name("Sm1th")
        with self.assertRaises(ValidationError):
            validate_last_name("Sm@th")

    def test_valid_phone(self):
        self.assertEqual(validate_phone("+380987654321"), "+380987654321")
        self.assertEqual(validate_phone("380987654321"), "380987654321")

    def test_invalid_phone(self):
        with self.assertRaises(ValidationError):
            validate_phone("++380987654321")
        with self.assertRaises(ValidationError):
            validate_phone("+38098765432a")
        with self.assertRaises(ValidationError):
            validate_phone("+3809876543211+")

    def test_valid_username(self):
        self.assertEqual(validate_username("ivan"), "ivan")
        self.assertEqual(validate_username("ivan_1"), "ivan_1")
        self.assertEqual(validate_username("ivan.1"), "ivan.1")

    def test_invalid_username(self):
        with self.assertRaises(ValidationError):
            validate_username(".ivan")
        with self.assertRaises(ValidationError):
            validate_username("_ivan")
        with self.assertRaises(ValidationError):
            validate_username("ivan..1")
        with self.assertRaises(ValidationError):
            validate_username("ivan__1")
        with self.assertRaises(ValidationError):
            validate_username("iv")
        with self.assertRaises(ValidationError):
            validate_username("ivan._1")
