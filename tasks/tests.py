from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='TestCategory')
        self.valid_payload = {
            'title': 'Test Title',
            'description': 'Test Description',
            'categories': [{'id': self.category.id}]
        }
        self.invalid_payload = {
            'title': '',
            'description': 'Invalid Description',
            'categories': [{'id': self.category.id}]
        }

    def test_create_valid_task(self):
        response = self.client.post('/api/tasks/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)

    def test_create_invalid_task(self):
        response = self.client.post('/api/tasks/', self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)

    def test_retrieve_task(self):
        task = Task.objects.create(title='Test Title', description='Test Description')
        url = f'/api/tasks/{task.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], task.title)
        self.assertEqual(response.data['description'], task.description)
