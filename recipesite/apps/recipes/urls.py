from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.showRecipes, name='showRecipes'),
    path('new', views.getRecipes, name='getRecipes'),
    re_path(r'^new/$', views.getRecipes),
    path('list', views.shoppingList, name='shoppingList'),
    # path('test', views.getRecipeTest, name='getRecipeTest'),
]