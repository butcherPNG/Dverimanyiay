from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=64, blank=False, unique=True)
    email = models.EmailField(verbose_name='Почта', max_length=64, blank=False, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=64, blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Door(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, blank=False)
    color = models.CharField(verbose_name='Цвет', max_length=200, blank=False)
    material = models.CharField(verbose_name='Материал', max_length=200, blank=False)
    size = models.CharField(verbose_name='Размер', max_length=200, blank=False)
    price = models.DecimalField(verbose_name='Цена', max_length=200, blank=True, max_digits=10, decimal_places=2, default=0)
    img = models.ImageField(verbose_name='Картинка', max_length=200, blank=False, upload_to='static/img')
    
    def __str__(self):
        return self.name + ', Материал: ' + self.material


class Delivery(models.Model):
    fullname = models.CharField(verbose_name='ФИО', max_length=200, blank=False)
    phone = models.CharField(verbose_name='Номер телефона', max_length=200, blank=False)
    address = models.CharField(verbose_name='Адрес', max_length=200, blank=False)
    date = models.DateField(verbose_name='Дата доставки', max_length=200, blank=False)

    def __str__(self):
        return 'Заказ от ' + self.fullname