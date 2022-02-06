from django.core.management.base import BaseCommand
import pandas as pd
from michelinapp.models import Recipes, Ingredients, Junction

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Database Connections
        df = pd.read_csv('ingredients.csv')
        for i,row in df.iterrows():
            models = Ingredients(i,row['name'],row['ingredient_id'])
            models.save()

        # name,minutes,n_steps,steps,description,ingredients,n_ingredients
        df = pd.read_csv('recipes.csv')
        for i,row in df.iterrows():
            models = Recipes(i, row['name'], row['minutes'], row['n_steps'], row['steps'], row['description'], row['ingredients'], row['n_ingredients'], row['recipe_id'])
            models.save()

        df = pd.read_csv('junction.csv')
        for i,row in df.iterrows():
            models = Junction(i, row['ingredient_id'], row['recipe_id'])
            models.save()
