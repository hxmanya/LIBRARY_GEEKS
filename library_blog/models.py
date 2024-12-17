from django.db import models

class BookModel(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Детектив', 'Детектив'),
        ('Приключения', 'Приключения')
    )
    image = models.ImageField(upload_to='book_images/', verbose_name='Загрузите фото книги')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание книги', blank=True)
    price = models.FloatField(verbose_name='Укажите цену книги', default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Фантастика')
    authors_mail = models.EmailField(max_length=100, blank=True, verbose_name='Укажите почту автора')
    author = models.CharField(max_length=100, verbose_name='Укажите имя автора')
    trailer = models.URLField(verbose_name='Укажите ссылку на видео', null=True)


    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title

class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    )
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    text_review = models.TextField(verbose_name='Напишите комментарий')
    stars = models.CharField(max_length=100, choices=STARS, verbose_name='Поставьте оценку', default='⭐')

    def __str__(self):
        return f'{self.book} - {self.stars}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"