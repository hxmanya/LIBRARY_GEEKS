# Generated by Django 5.1.4 on 2024-12-12 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0002_bookmodel_trailer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'книгу', 'verbose_name_plural': 'книги'},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text_review', models.TextField(verbose_name='Напишите комментарий')),
                ('stars', models.CharField(default='⭐', max_length=100, verbose_name='Поставьте оценку')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='library_blog.bookmodel')),
            ],
        ),
    ]
