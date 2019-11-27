from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from ...main.models import Tag

from ..serializers import TagSerializer

TAGS_URL = reversed('recipe:tag-list')