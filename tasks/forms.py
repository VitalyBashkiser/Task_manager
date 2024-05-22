from ckeditor.widgets import CKEditorWidget
from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
