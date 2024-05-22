from django.test import TestCase
from django.urls import reverse
from tasks.models import Task, Tag
from django.contrib.auth.models import User
from django.utils import timezone


class TaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.tag = Tag.objects.create(name="Home")
        self.task = Task.objects.create(
            content="Test task",
            deadline=timezone.now() + timezone.timedelta(days=1),
            is_done=False,
            user=self.user
        )
        self.task.tags.add(self.tag)

    def test_task_list_view(self):
        response = self.client.get(reverse('tasks:task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test task")

    def test_task_create_view(self):
        response = self.client.post(reverse('tasks:task-add'), {
            'content': 'New task',
            'deadline': '2024-05-23 23:59:00',
            'is_done': False,
            'tags': [self.tag.id],
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update_view(self):
        response = self.client.post(reverse('tasks:task-update', args=[self.task.id]), {
            'content': 'Updated task',
            'deadline': '2024-05-23 23:59:00',
            'is_done': True,
            'tags': [self.tag.id],
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, 'Updated task')
        self.assertTrue(self.task.is_done)

    def test_task_delete_view(self):
        response = self.client.post(reverse('tasks:task-delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)


class TagViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.tag = Tag.objects.create(name="Home")

    def test_tag_list_view(self):
        response = self.client.get(reverse('tasks:tag-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")

    def test_tag_create_view(self):
        response = self.client.post(reverse('tasks:tag-add'), {'name': 'Work'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 2)

    def test_tag_update_view(self):
        response = self.client.post(reverse('tasks:tag-update', args=[self.tag.id]), {'name': 'Updated Tag'})
        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, 'Updated Tag')

    def test_tag_delete_view(self):
        response = self.client.post(reverse('tasks:tag-delete', args=[self.tag.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 0)
