# Generated by Django 5.0.6 on 2024-06-20 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_order_alter_financialtransaction_order_and_more'),
        ('orders', '0011_remove_buy_price_remove_buy_year_remove_buy_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='order',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Shipment',
        ),
    ]
