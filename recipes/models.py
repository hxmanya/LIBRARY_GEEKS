from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def total_calories(self):
        return sum(ingredient.calories for ingredient in self.ingredients.all())

    def __str__(self):
        return self.title

class Collection(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe, related_name='collections')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('g', 'граммы'),
        ('kg', 'килограммы'),
        ('ml', 'миллилитры'),
        ('l', 'литры'),
        ('pcs', 'штуки'),
    ]

    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    is_optional = models.BooleanField(default=False)
    calories = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.get_unit_display()})"


# Create your models here.
