# Generated by Django 5.1.4 on 2024-12-19 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0007_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]