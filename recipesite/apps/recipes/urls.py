from django.urls import path

from . import views

urlpatterns = [
    path('', views.showRecipes, name='showRecipes'),
    path('new', views.getRecipes, name='getRecipes'),
    path('list', views.shoppingList, name='shoppingList'),
    # path('test', views.getRecipeTest, name='getRecipeTest'),
]