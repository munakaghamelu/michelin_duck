from django.shortcuts import render
from .models import Ingredients, Recipes, Junction

# Create your views here.


def index(request):
    return render(request, 'michelinapp/index.html')


def add_inrediant(request):
    return


def delete_ingrediant(request):
    return


def get_recipe(request):
    ingredients = request.GET.get('ingredient')
    ingredients = ingredients.split(",")

    ingID = Ingredients.objects.filter(name__in=ingredients)
    ingredients = []
    for ingredient in ingID:
        print(ingredient.ingredient_id)
        print(ingredient.name)
        ingredients.append(ingredient.ingredient_id)

    pair = Junction.objects.filter(ingredient_id__in=ingredients)
    recipes = []
    for recipe_id in pair:
        recipes.append(recipe_id.recipe_id)
    print(recipes)

    recipes = Recipes.objects.filter(id__in=recipes)
    print(recipes)

    for r in recipes:
        print(r.recipe_id)
        print(r.name)

    return render(request, 'michelinapp/recipe.html', {'recipe': ingredients})
