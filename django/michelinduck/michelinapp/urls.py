from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe', views.get_recipe, name='recipe')
]
