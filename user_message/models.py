from django.db import models
from django.core.validators import RegexValidator


class UserMessage(models.Model):
    email_re = RegexValidator(regex=r'^[^W_]\w+-?\w+@[a-z]+(\.[a-zA-Z0-9]+)*$', message='Невірний формат Email')

    name = models.CharField("Ім'я", max_length=50)
    email = models.EmailField('Email', validators=[email_re])
    topic = models.CharField('Тема', max_length=150)
    message = models.TextField('Повідомлення', max_length=500)

    archived = models.BooleanField('У архіві', default=False)
    date_in = models.DateTimeField('дата створення', auto_now_add=True)
    date_archiving = models.DateTimeField('остання дія', auto_now=True)

    class Meta:
        verbose_name = 'Повідомлення від клієнта'
        verbose_name_plural = 'Повідомлення від клієнта'
        ordering = ('archived', )

    def __str__(self):
        return f'{self.name} ({self.email}), {self.topic}: {self.message[:20]}'
