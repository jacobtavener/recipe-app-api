from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Artist

from album.serializers import ArtistSerializer


ARTIST_URL = reverse('album:artist-list')


class PublicArtistsApiTests(TestCase):
    """Test the publicly available artist API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access the endpoint"""
        res = self.client.get(ARTIST_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateArtistsApiTests(TestCase):
    """Test the private artists API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@test_email.com',
            'testpass123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_artist_list(self):
        """Test retrieving a list of artists"""
        Artist.objects.create(user=self.user, name='Muddy Waters')
        Artist.objects.create(user=self.user, name='B.B King')

        res = self.client.get(ARTIST_URL)

        artists = Artist.objects.all().order_by('-name')
        serializer = ArtistSerializer(artists, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_artist_limited_to_user(self):
        """Test that artists for the authenticated user are returned"""
        user2 = get_user_model().objects.create_user(
            'other_test@test_email.com',
            'otherpass123'
        )
        Artist.objects.create(user=user2, name='Howlin Wolf')
        ingredient = Artist.objects.create(user=self.user, name='Albert King')

        res = self.client.get(ARTIST_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)
