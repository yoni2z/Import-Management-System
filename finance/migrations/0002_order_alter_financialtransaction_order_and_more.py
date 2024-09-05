# Generated by Django 5.0.6 on 2024-06-20 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrations', '0005_alter_cars_model_specifications_and_more'),
        ('finance', '0001_initial'),
        ('orders', '0011_remove_buy_price_remove_buy_year_remove_buy_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrations.cars_model')),
                ('TrackingNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.importorder')),
            ],
        ),
        migrations.AlterField(
            model_name='financialtransaction',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance.order'),
        ),
        migrations.AlterField(
            model_name='taxrecord',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tax_records', to='finance.order'),
        ),
    ]