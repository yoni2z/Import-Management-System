# Generated by Django 5.0.6 on 2024-06-20 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_alter_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='model',
            new_name='Model',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='trackingNo',
            new_name='TrackingNo',
        ),
    ]