# Generated by Django 5.0.6 on 2024-06-18 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_imports_importorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importorder',
            name='Count',
        ),
    ]