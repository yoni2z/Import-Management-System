# Generated by Django 5.0.6 on 2024-06-20 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminstrations', '0005_alter_cars_model_specifications_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color', models.CharField(default='Unspecified', max_length=50)),
                ('Count', models.PositiveIntegerField()),
                ('Model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrations.cars_model')),
            ],
        ),
    ]
