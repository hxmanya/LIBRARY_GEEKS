# Generated by Django 5.1.4 on 2024-12-13 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0005_remove_review_film_review_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
