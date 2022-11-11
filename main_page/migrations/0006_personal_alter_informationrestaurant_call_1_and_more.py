# Generated by Django 4.1.3 on 2022-11-10 22:39

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_informationrestaurant_is_visible_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=25, verbose_name='Прізвище')),
                ('major', models.CharField(max_length=50, verbose_name='Спеціальність')),
                ('photo', models.ImageField(upload_to=main_page.models.Personal.get_file_name, verbose_name='Фото')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Номер телефону')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Відображення')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
                'ordering': ('surname',),
            },
        ),
        migrations.AlterField(
            model_name='informationrestaurant',
            name='call_1',
            field=models.CharField(max_length=15, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='informationrestaurant',
            name='call_2',
            field=models.CharField(blank=True, default=True, max_length=15, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='informationrestaurant',
            name='post_index',
            field=models.CharField(max_length=15, verbose_name='поштовий індекс'),
        ),
    ]
