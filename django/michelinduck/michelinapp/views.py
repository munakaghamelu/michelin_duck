from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'michelinapp/index.html')


def add_inrediant(request):
    return


def delete_ingrediant(request):
    return


def get_recipe(request):
    ingredient = request.GET.get('ingredient')

    return render(request, 'michelinapp/recipe.html', {'recipe': ingredient})
