from django.db import models
import uuid
import os


class Category(models.Model):
    title = models.CharField('Назва категорії', max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField('Відображення', default=True)
    position = models.PositiveSmallIntegerField('Позиція відображення', unique=True)

    class Meta:
        verbose_name = 'Категорія меню'
        verbose_name_plural = 'Категорії меню'
        ordering = ('position', )

    def __str__(self):
        return f'{self.title}: {self.position}'


class Dish(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/dishes', fr'{uuid.uuid4()}.{ext}')

    title = models.CharField('Назва страви', max_length=50, unique=True, db_index=True)
    ingredients = models.CharField('Склад страви', max_length=150)
    price = models.DecimalField('Ціна', max_digits=8, decimal_places=2)
    is_special = models.BooleanField('Входить до спеціальної пропозиції', default=False)
    is_visible = models.BooleanField('Вдображення', default=True)
    position = models.PositiveSmallIntegerField('Позиція')
    desc = models.TextField('Опис страви', max_length=500, blank=True)
    photo = models.ImageField('Фото страви', upload_to=get_file_name)
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ('position', )

    def __str__(self):
        return f'{self.title}'


class Event(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/event', fr'{uuid.uuid4()}.{ext}')

    title = models.CharField('Назва заходу', max_length=50, unique=True, db_index=True)
    price = models.DecimalField('Вартість', max_digits=8, decimal_places=2)
    description = models.TextField('Опис', max_length=1000, blank=True)
    image = models.ImageField('Титульне фото', upload_to=get_file_name)
    date = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Захід'
        verbose_name_plural = 'Заходи'

    def __str__(self):
        return f'{self.title}'


class All_Inform(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/restaurant', fr'{uuid.uuid4()}.{ext}')

    title = models.CharField('Заголовок', max_length=200, unique=True)
    description = models.TextField('Опис')
    link_video = models.URLField('Посилання на відео', blank=True)
    photo = models.ImageField('Фото', upload_to=get_file_name, blank=True)
    is_visible = models.BooleanField('Відображення "чому ми"', default=False)
    position = models.PositiveSmallIntegerField('Позиция', blank=True)

    class Meta:
        verbose_name = 'Про ресторан'
        verbose_name_plural = 'Про ресторан'
        ordering = ('position', )

    def __str__(self):
        return f'{self.title}: {self.position}'


class Gallery(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/gallery', fr'{uuid.uuid4()}.{ext}')

    photo = models.ImageField('фото', upload_to=get_file_name)
    is_visible = models.BooleanField('відображення')
    desc = models.CharField(max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галерея'
        ordering = ('pk', )

    def __str__(self):
        return f'фото-{self.pk}'


class InformationRestaurant(models.Model):
    is_visible = models.BooleanField('активне', default=False)
    location_city = models.CharField('місто', max_length=50)
    location = models.CharField('адреса', max_length=250)
    post_index = models.CharField('поштовий індекс', max_length=15)
    open_days_start = models.CharField('перший робочий день', max_length=15)
    open_days_end = models.CharField('останній робочий день', max_length=15)
    open_hours_start = models.TimeField('початок робочого дня')
    open_hours_end = models.TimeField('кінець робочого дня')
    e_mail_1 = models.EmailField('перший E_mail')
    e_mail_2 = models.EmailField('другий E_mail', blank=True, default='')
    call_1 = models.CharField('номер телефона', max_length=15)
    call_2 = models.CharField('номер телефона', max_length=15, blank=True, default=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    skype = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name = 'загальна інформація ресторану'
        verbose_name_plural = 'загальна інформація ресторану'

    def __str__(self):
        return f'варіант {self.pk}'


class Personal(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/personal', fr'{uuid.uuid4()}.{ext}')

    name = models.CharField("Ім'я", max_length=20)
    surname = models.CharField('Прізвище', max_length=25)
    major = models.CharField('Спеціальність', max_length=50)
    photo = models.ImageField('Фото', upload_to=get_file_name)
    phone = models.CharField('Номер телефону', max_length=15, blank=True)
    is_visible = models.BooleanField('Відображення', default=True)

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        ordering = ('surname', )

    def __str__(self):
        return f'{self.name} {self.surname}'


class Testimonials(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/testimonials', fr'{uuid.uuid4()}.{ext}')

    name = models.CharField("ім'я", max_length=25)
    surname = models.CharField('Прізвище', max_length=25)
    major = models.CharField('Посада', max_length=30)
    desc = models.TextField('Відгук', max_length=1000)
    is_visible = models.BooleanField('Відображення', default=True)
    photo = models.ImageField('Фото', upload_to=get_file_name)

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f'Відгук {self.pk}'


class HeroSection(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/slides', fr'{uuid.uuid4()}.{ext}')

    title = models.CharField('Заголовок', max_length=50, unique=True)
    desc = models.TextField('Опис', max_length=300)
    photo = models.ImageField('Фото', upload_to=get_file_name)
    is_visible = models.BooleanField('Відображення', default=True)

    class Meta:
        verbose_name = 'слайди у шапці'
        verbose_name_plural = 'слайди у шапці'

    def __str__(self):
        return f'{self.title}'

