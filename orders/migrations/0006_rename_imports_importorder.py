# Generated by Django 5.0.6 on 2024-06-18 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_importorder_imports'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='imports',
            new_name='importOrder',
        ),
    ]