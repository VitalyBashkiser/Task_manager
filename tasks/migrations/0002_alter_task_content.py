# Generated by Django 5.0.6 on 2024-05-22 08:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
