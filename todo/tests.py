# todo/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTests(TestCase):
    def test_create_task_with_title(self):
        """Test creating a task with just a title"""
        task = Task.objects.create(title="Test task")
        self.assertEqual(task.title, "Test task")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_date)

class TaskViewsTests(TestCase):
    def test_create_task_view(self):
        """Test the task creation view"""
        response = self.client.post(reverse('create_task'), {'title': 'New task'})
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'New task')