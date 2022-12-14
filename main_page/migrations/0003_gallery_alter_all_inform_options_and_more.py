# Generated by Django 4.1.3 on 2022-11-09 17:22

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_all_inform_event_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=main_page.models.Gallery.get_file_name, verbose_name='фото')),
                ('is_visible', models.BooleanField(verbose_name='відображення')),
                ('desc', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'галерея',
                'verbose_name_plural': 'галерея',
            },
        ),
        migrations.AlterModelOptions(
            name='all_inform',
            options={'ordering': ('position',), 'verbose_name': 'Про ресторан', 'verbose_name_plural': 'Про ресторан'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name': 'Категорія меню', 'verbose_name_plural': 'Категорії меню'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('position',), 'verbose_name': 'Страва', 'verbose_name_plural': 'Страви'},
        ),
        migrations.AlterField(
            model_name='all_inform',
            name='desc',
            field=models.TextField(max_length=10000, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='all_inform',
            name='is_visible',
            field=models.BooleanField(default=False, verbose_name='Відображення "чому ми"'),
        ),
        migrations.AlterField(
            model_name='all_inform',
            name='photo',
            field=models.ImageField(blank=True, upload_to=main_page.models.All_Inform.get_file_name, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='all_inform',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Відображення'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Опис'),
        ),
    ]
