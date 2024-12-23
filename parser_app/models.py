from django.db import models

class MyBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.title