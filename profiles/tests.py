import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'testcase',
                'email': 'test@local.com',
                'password1': 'bomuca123',
                'password2': 'bomuca123',}
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
class ProfileViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='davinci',
                                             password='bomuca123')
        self.token = Token.objects.create(user=self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=)