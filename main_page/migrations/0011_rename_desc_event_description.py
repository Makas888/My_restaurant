# Generated by Django 4.1.3 on 2022-11-13 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0010_alter_all_inform_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='desc',
            new_name='description',
        ),
    ]