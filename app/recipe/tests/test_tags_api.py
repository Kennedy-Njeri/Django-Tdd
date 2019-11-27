from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from ...main.models import Tag

from ..serializers import TagSerializer

TAGS_URL = reversed('recipe:tag-list')


class PublicTagsApiTests(TestCase):
    """Test the publicly available tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateTagsApiTests(TestCase):
    """Test the authorized user"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'mistakenz@gmail.com',
            'password1234'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
