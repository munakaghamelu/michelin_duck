from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipebook', views.get_recipe_names, name='recipebook'),
    path('recipe', views.get_recipe, name='recipe'),
]
