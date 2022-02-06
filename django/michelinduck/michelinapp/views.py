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


def get_recipe(request):
    # recipe_id = request.GET.get('recipe_id')
    recipe = Recipes.objects.get(id='3')
    steps = recipe.steps
    steps = steps[1:-1].split(",")

    dangerous = ["cut", "heat", "fry", "cook", "knife",
                 "bake", "chop", "kill", "oven", "boil", "burn"]

    safe = [0 for _ in range(len(steps))]
    print(safe)

    steps[0] = steps[0][1:-1]

    for i in range(1, len(steps)):
        steps[i] = steps[i][2:-1]
        if any(word in steps[i] for word in dangerous):
            safe[i] = 1
    print(steps)

    for i in range(len(steps)):
        print(str(safe[i]) + " : " + steps[i])

    result = list(zip(steps, safe))
    print(result)

    return render(request, 'michelinapp/recipe.html', {'result': result})


def evaluate_safety(request):
    return
