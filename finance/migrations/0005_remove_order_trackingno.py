# Generated by Django 5.0.6 on 2024-06-20 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_order_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='TrackingNo',
        ),
    ]