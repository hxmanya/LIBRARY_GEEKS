from django.db import models
from age_limit.models import Book


class Basket(models.Model):
    name = models.CharField(max_length=100, verbose_name='Укажите ваше имя')
    email = models.EmailField(max_length=100, verbose_name='Укажите почту')
    phone_number = models.CharField(max_length=15, verbose_name='Укажите номер телефона')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Выберите книгу')

    def __str__(self):
        return f"Заказ {self.name} на книгу {self.book.title}"
