# Generated by Django 4.1.3 on 2022-11-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_rename_desc_all_inform_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_inform',
            name='description',
            field=models.TextField(verbose_name='Опис'),
        ),
    ]
