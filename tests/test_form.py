from django.test import TestCase
from tasks.forms import TaskForm, TagForm


class TaskFormTest(TestCase):
    def test_task_form_valid(self):
        form_data = {
            'content': 'Test task',
            'deadline': '2024-05-22 12:00:00',
            'is_done': False,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form_data = {
            'content': '',
            'deadline': 'invalid-date',
            'is_done': False,
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())


class TagFormTest(TestCase):
    def test_tag_form_valid(self):
        form_data = {
            'name': 'Test tag',
        }
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_form_invalid(self):
        form_data = {
            'name': '',
        }
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())
