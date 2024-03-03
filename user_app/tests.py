from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


# Create your tests here.

class RegisterTestCase(APITestCase):
    def test_signup(self):
        data = {
            "username": "testcase",
            "email": "kferdoush617@gmail.com",
            "password": "some_strong_psw",
            "password2": "some_strong_psw",

        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 201)


class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='some_strong_psw')

    def test_login(self):
        data = {
            "username": "testuser",
            "password": "some_strong_psw"
        }
        response = self.client.post(reverse('login'), data)
        self.client.post(reverse(response.status_code, status.HTTP_200_OK))

    def test_logout(self):
        self.token = Token.objects.get(user__username='testuser')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

