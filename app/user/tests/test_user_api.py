from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().object.create_user(**params)


class PublicUserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpas123',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
