from django.shortcuts import render

# Create your views here.

def recipes(request):
    return render(request, 'recipes/recipes.html')

def getRecipe(request):
    return render(request, 'recipes/recipes.html')