from django.test import TestCase
from tasks.models import Task, Tag


class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(content='Test task', deadline='2024-05-22 12:00:00', is_done=False)
        self.assertEqual(task.content, 'Test task')
        self.assertEqual(task.is_done, False)

    def test_create_task_without_deadline(self):
        task = Task.objects.create(content='Test task without deadline', is_done=False)
        self.assertEqual(task.content, 'Test task without deadline')
        self.assertIsNone(task.deadline)


class TagModelTest(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name='Test tag')
        self.assertEqual(tag.name, 'Test tag')
