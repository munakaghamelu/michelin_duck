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
    for id in ingID:
        print(id.id)

    return render(request, 'michelinapp/recipe.html', {'recipe': ingredients})
