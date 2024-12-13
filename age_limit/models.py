from django.db import models

from library_blog.models import BookModel


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)#, related_name='books')
    price = models.FloatField(default=10)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.book.title