from django.shortcuts import render
from .models import Ingredients, Recipes, Junction

# Create your views here.


def index(request):
    return render(request, 'michelinapp/index.html')


def add_inrediant(request):
    return


def delete_ingrediant(request):
    return


def get_recipe_names(request):
    ingredients = request.GET.get('ingredient')
    ingredients = ingredients.split(",")

    ingredients_items = Ingredients.objects.filter(name__in=ingredients)
    ingredients_ids = []
    for ingredient in ingredients_items:
        ingredients_ids.append(ingredient.ingredient_id)

    matched_recipes = []
    for ingredients_id in ingredients_ids:
        recipes = Junction.objects.filter(ingredient_id=ingredients_id)
        recipe_ids = []
        for recipe in recipes:
            recipe_ids.append(recipe.recipe_id)
        matched_recipes.append(recipe_ids)
    
    best_matched_recipes = list(set.intersection(*map(set, matched_recipes)))
    recipes = Recipes.objects.filter(id__in=best_matched_recipes)

    return render(request, 'michelinapp/recipebook.html', {'recipes': recipes})


def get_recipe(request):
    recipe_id = request.GET.get('select')
    print(recipe_id)
    return render(request, 'michelinapp/recipe.html', {'recipe':recipe_id})