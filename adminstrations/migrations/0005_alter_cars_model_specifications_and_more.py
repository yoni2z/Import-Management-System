# Generated by Django 5.0.6 on 2024-06-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrations', '0004_alter_supplier_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars_model',
            name='Specifications',
            field=models.CharField(choices=[('fuel', 'FUEL'), ('electric', 'ELECTRIC')], max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='country',
            field=models.CharField(choices=[('japan', 'JAPAN'), ('germany', 'GERMANY'), ('southkorea', 'SOUTH KOREA')], max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supp_name',
            field=models.CharField(choices=[('hyundai', 'HYUNDAI'), ('honda', 'HONDA'), ('toyota', 'TOYOTA'), ('volkswagen', 'VOLKSWAGEN')], max_length=20),
        ),
    ]
