from django.db import models
from django.core.validators import RegexValidator


class UserReservation(models.Model):
    mobile_phone_re = RegexValidator(regex=r'^380\d{2}( -)?\d{7}$', message='Невірний формат номеру телефона')
    email_re = RegexValidator(regex=r'^[^W_]\w+-?\w+@[a-z]+(\.[a-zA-Z0-9]+)*$', message='Невірний формат Email')
    
    name = models.CharField("Ім'я", max_length=50)
    email = models.EmailField('Email', validators=[email_re])
    phone = models.CharField('Телефон', max_length=15, validators=[mobile_phone_re])
    date_order = models.DateField('Дата')
    time_order = models.TimeField('час')
    persons = models.PositiveSmallIntegerField('кількість людей')
    massage = models.TextField('Повідомлення', max_length=1000)

    is_processing = models.BooleanField('Опрацьованно', default=False)
    date_in = models.DateTimeField('дата реєстрації', auto_now_add=True)
    date_modify = models.DateTimeField('останнє опрацювання', auto_now=True)

    class Meta:
        ordering = ('-date_in', )
        verbose_name = ('Бронювання')
        verbose_name_plural = ('Бронювання')

    def __str__(self):
        return f'{self.name}: {self.phone}: {self.massage[:20]}'
    