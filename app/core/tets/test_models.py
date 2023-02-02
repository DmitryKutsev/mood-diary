"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_positive(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@EXAMPLE.COM', 'test2@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample12')
            self.assertEqual(user.email, expected)
            self.assertFalse(user.is_superuser)
            self.assertFalse(user.is_volunteer)

    def test_create_volunteer(self):
        """Test creating a superuser."""

        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_volunteer(
            email=email,
            password=password,
        )
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_volunteer)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_create_superuser(self):
        """Test creating a superuser."""

        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_volunteer)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
