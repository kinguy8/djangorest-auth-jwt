from django.db import models
#from django.contrib.auth import get_user_model
from users.models import User


class Film(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    content = models.TextField(verbose_name="Описание", blank=True)
    year = models.IntegerField(verbose_name="Год")
    time_create = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Время изменения", auto_now=True)
    is_published = models.BooleanField(verbose_name="Публичность", default=True)
    genre = models.ForeignKey('Genres', verbose_name="Жанр",  on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT)

    def __str__(self):
        """Вывод заголовка из текущей записи"""
        return self.title


class Genres(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
