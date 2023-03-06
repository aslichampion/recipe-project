from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.show_recipes, name='showRecipes'),
    path('new', views.get_recipes, name='getRecipes'),
    re_path(r'^new/$', views.get_recipes),
    path('list', views.shopping_list, name='shoppingList'),
    # path('test', views.getRecipeTest, name='getRecipeTest'),
]
