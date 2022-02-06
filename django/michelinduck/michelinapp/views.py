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
    ingredients = "('" + ingredients[0] + "',)"

    ingID = Ingredients.objects.all(name__in="('" + ingredients[0] + "',)")
    print(ingID[0])

    return render(request, 'michelinapp/recipe.html', {'recipe': ingredients})
