from django.test import TestCase
from tasks.forms import TaskForm, TagForm


class TaskFormTest(TestCase):

    def test_task_form_invalid(self):
        form_data = {
            "content": "",
            "deadline": "invalid-date",
            "is_done": False,
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())


class TagFormTest(TestCase):

    def test_tag_form_invalid(self):
        form_data = {
            "name": "",
        }
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())

