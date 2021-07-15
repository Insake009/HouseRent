from django.db import models
from .constants import CITY, QUANTITY_OF_ROOMS
from users.models import User

class House(models.Model):
    image = models.ImageField(upload_to='house', verbose_name='Фото')
    city = models.CharField(choices=CITY, max_length=11, verbose_name='Город')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    area = models.IntegerField(verbose_name='Площадь')
    quantity_of_rooms = models.CharField(choices=QUANTITY_OF_ROOMS, max_length=9,verbose_name='Количество комнат')
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')
    user_id = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE,)
    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

    def __str__(self):
        return f'{self.quantity_of_rooms} / {self.price}$'

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    timestamp = models.DateTimeField(auto_now=True)
    house_id = models.ForeignKey(House, related_name='hous_id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return str(self.house_id)

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    like = models.BooleanField(default=False, verbose_name='Лайк')
    timestamp = models.DateTimeField(auto_now=True)
    house_id = models.ForeignKey(House, related_name='house_id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return str(self.house_id)