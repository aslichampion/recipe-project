from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('new', views.getRecipe, name='getRecipe'),
]