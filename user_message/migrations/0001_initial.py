# Generated by Django 4.1.3 on 2022-11-15 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator(message='Невірний формат Email', regex='^[^W_]\\w+-?\\w+@[a-z]+(\\.[a-zA-Z0-9]+)*$')], verbose_name='Email')),
                ('topic', models.CharField(max_length=150, verbose_name='Тема')),
                ('message', models.TextField(max_length=500, verbose_name='Повідомлення')),
                ('archived', models.BooleanField(default=False, verbose_name='У архіві')),
                ('date_in', models.DateTimeField(auto_now_add=True, verbose_name='дата створення')),
                ('date_archiving', models.DateTimeField(auto_now=True, verbose_name='остання дія')),
            ],
            options={
                'verbose_name': 'Повідомлення від клієнта',
                'verbose_name_plural': 'Повідомлення від клієнта',
                'ordering': ('archived',),
            },
        ),
    ]