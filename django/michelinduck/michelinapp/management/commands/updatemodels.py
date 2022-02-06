from django.core.management.base import BaseCommand
import pandas as pd
from michelinapp.models import Recipes, Ingredients, Junction

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #Database Connections
        df=pd.read_csv('ingredients.csv')
        for A in zip(df.name):
            models = Ingredients(name=A.strip("(',)"))
            models.save()

        # name,minutes,n_steps,steps,description,ingredients,n_ingredients
        df=pd.read_csv('recipes.csv')
        for A,B,C,D,E,F,G in zip(df.name,df.minutes,df.n_steps,df.steps,df.description,df.ingredients,df.n_ingredients):
            models = Recipes(name=A,minutes=B,n_steps=C,steps=D,description=E,ingredients=F,n_ingredients=G)
            models.save()

        df=pd.read_csv('junction.csv')
        for A,B in zip(df.ingredient_id,df.recipe_id):
            models = Junction(ingredient_id=A,recipe_id=B)
            models.save()
