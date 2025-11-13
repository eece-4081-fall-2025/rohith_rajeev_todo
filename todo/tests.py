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

    def test_task_list_view(self):
        """Test displaying all tasks in a list"""
        Task.objects.create(title="Task 1")
        Task.objects.create(title="Task 2")
        
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

    def test_mark_task_completed(self):
        """Test marking a task as completed"""
        task = Task.objects.create(title="Incomplete task")
        self.assertFalse(task.completed)
        
        # Update to completed
        task.completed = True
        task.save()
        
        updated_task = Task.objects.get(pk=task.pk)
        self.assertTrue(updated_task.completed)