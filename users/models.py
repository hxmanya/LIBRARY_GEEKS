from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    LVLS = (
        ('Ниже Junior', 'Ниже Junior'),
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    )

    phone_number = models.CharField(max_length=14)
    lvl = models.CharField(max_length=20, choices=LVLS)
    age = models.PositiveIntegerField(default=18)
    salary = models.CharField(max_length=50, default='зп не определена')

    def save(self, *args, **kwargs):
        if self.lvl == 'Ниже Junior':
            self.salary =  'Пожалуста подтяните ваш уровень'
        elif self.lvl == 'Junior':
            self.salary = '700$'
        elif self.lvl == 'Middle':
            self.salary = '1000$'
        elif self.lvl == 'Senior':
            self.salary = '2000$'
        else:
            self.salary = 'Ваш уровень нам не понятен, вы не подходите'

        super().save(*args, **kwargs)
