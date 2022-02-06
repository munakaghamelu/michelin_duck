from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class Ingredients(models.Model):
    name=models.CharField(max_length=50)
    ingredients_id=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Recipes(models.Model):
    name=models.CharField(max_length=100)
    minutes=models.IntegerField()
    n_steps=models.IntegerField()
    steps=models.CharField(max_length=1000)
    description=models.CharField(max_length=500)
    ingredients=models.CharField(max_length=1000)
    n_ingredients=models.IntegerField()
    recipe_id=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Junction(models.Model):
    ingredient_id=models.CharField(max_length=20)
    recipe_id=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.ingredient_id} and {self.recipe_id}'


