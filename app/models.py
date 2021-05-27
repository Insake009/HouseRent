from django.db import models
from users.models import User
from .constants import CITY, QUANTITY_OF_ROOMS

class House(models.Model):
    image = models.ImageField(upload_to='house', verbose_name='Фото')
    city = models.CharField(choices=CITY, max_length=11, verbose_name='Город')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    area = models.IntegerField(verbose_name='Площадь')
    quantity_of_rooms = models.CharField(choices=QUANTITY_OF_ROOMS, max_length=9,verbose_name='Количество комнат')
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')
    users_id = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE, default=True)

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

    def __str__(self):
        return f'{self.quantity_of_rooms} / {self.price}$'
