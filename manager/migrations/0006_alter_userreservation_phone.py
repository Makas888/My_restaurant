# Generated by Django 4.1.3 on 2022-11-15 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_rename_date_order_userreservation_date_reserve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Невірний формат номеру телефона', regex='^[+]?380\\d{2}( -)?\\d{7}$')], verbose_name='Телефон'),
        ),
    ]