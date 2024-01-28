from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import CustomUser

class UserAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_user_url = reverse('create_user')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'balance': '100.00'
        }
        self.existing_user = CustomUser.objects.create(username='existinguser', email='existing@example.com', balance=50.00)

    def test_create_user_success(self):
        response = self.client.post(self.create_user_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User registered successfully.")

    def test_create_user_existing_email(self):
        self.user_data['email'] = self.existing_user.email 
        response = self.client.post(self.create_user_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_success(self):
        retrieve_user_url = reverse('rUser', kwargs={'username': self.existing_user.username})
        response = self.client.get(retrieve_user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.existing_user.username)

    def test_retrieve_user_not_found(self):
        retrieve_user_url = reverse('rUser', kwargs={'username': 'nonexistentuser'})
        response = self.client.get(retrieve_user_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

