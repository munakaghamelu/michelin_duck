from configparser import SafeConfigParser
import re
from django.shortcuts import render
from .models import Ingredients, Recipes, Junction

# Create your views here.


def index(request):
    return render(request, 'michelinapp/index.html')


def add_ingredient(request):
    return


def delete_ingrediant(request):
    return

def getTechniques(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = Recipes.objects.get(in__id=recipe_id)
    steps = recipe.steps
    # steps = steps[1:-1].split(",")
    # steps[0] = steps[0][1:-1]
    # for i in range(1, len(steps)):
    #     steps[i] = steps[i][2:-1]

    steps = str(steps)

    techniques = ["mix", "stir", "tear", "assemble", "mash", "roll",
                  "spread", "peel", "sift", "drain", "knead", "season", "garnish"]

    learn = []

    for t in techniques:
        if t in steps:
            learn.append(t)

    return

def get_recipe(request):
    recipe_id = request.GET.get('select')
    recipe = Recipes.objects.get(id=recipe_id)
    steps = recipe.steps

    techniques = ["mix", "stir", "tear", "assemble", "mash", "roll",
                  "spread", "peel", "sift", "drain", "knead", "season", "garnish"]

    learn = []

    for t in techniques:
        if t in steps:
            learn.append(t)

    steps = steps[1:-1].split(",")

    dangerous = ["cut", "heat", "fry", "cook", "knife",
                 "bake", "chop", "kill", "oven", "boil", "burn"]

    safe = [0 for _ in range(len(steps))]
    # print(safe)

    steps[0] = steps[0][1:-1]

    for i in range(1, len(steps)):
        steps[i] = steps[i][2:-1]
        if any(word in steps[i] for word in dangerous):
            safe[i] = 1
    # print(steps)
    
    for i in range(len(steps)):
        print(str(safe[i]) + " : " + steps[i])

    result = list(zip(steps, safe))
    # print(result)
    ingredients = recipe.ingredients
    ingredients = ingredients.replace('[','')
    ingredients = ingredients.replace(']','')
    ingredients = ingredients.replace('\'','')
    ingredients_list = ingredients.split(',')
    print(ingredients_list)
    return render(request, 'michelinapp/recipe.html', {'result': result, 'ingredients': ingredients_list, 'learn': learn})

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
