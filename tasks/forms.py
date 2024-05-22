<<<<<<< HEAD
from bootstrap_datepicker_plus.widgets import DatePickerInput
from ckeditor.widgets import CKEditorWidget
from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorWidget(attrs={"class": "form-control"})
    )
    deadline = forms.DateTimeField(
        widget=DatePickerInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker",
            }
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
=======
>>>>>>> parent of fe26dee (Edit models, forms, urls)
