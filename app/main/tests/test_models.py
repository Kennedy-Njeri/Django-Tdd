from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Tag


def sample_user(email='mistakenz@gmail.com', password='password123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with email"""
        email = "mistakenz@gmail.com"
        password = "29397252"
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "mista@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email,
            "1234ken")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "1234Ken")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'mistakenz@gmail.com',
            '1234Ken')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = Tag.objects.create(
            user=sample_user(),
            name='cabbage'
        )

        self.assertEqual(str(tag), tag.name)
