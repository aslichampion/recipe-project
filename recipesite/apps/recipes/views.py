from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
from decouple import config

# Create your views here.

def recipes(request):
    return render(request, 'recipes/recipes.html')

def getRecipe(request):
    apiLink = "https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&health=vegetarian&mealType=Dinner&random=true".format(config('API_ID'), config('API_KEY'))
    apiResponse = requests.get(apiLink)
    recipes = json.loads(apiResponse.text)
    recipeTitle = (recipes["hits"][0]["recipe"]["label"])
    template = loader.get_template('recipes/recipes.html')
    context = {
        'recipeTitle': recipeTitle,
    }
    return HttpResponse(template.render(context, request))
    
    
    # return render(request, 'recipes/recipes.html')

# print(getRecipe())
# recipe1 = getRecipe()
# print(recipe1["label"])

# print(recipes == apiResponse.json())
# print(recipes["hits"][0]["recipe"]["label"])
# print(recipes["hits"][0]["recipe"]["ingredientLines"])
# print(recipes["hits"][0]["recipe"]["source"])
# print(recipes["hits"][0]["recipe"]["url"])

# print(recipes["hits"][0]["recipe"]["ingredients"][0]["food"])
# print(recipes["hits"][0]["recipe"]["ingredients"][0]["measure"])
# print(recipes["hits"][0]["recipe"]["ingredients"][0]["quantity"])
# print(recipes["hits"][0]["recipe"]["ingredients"][0]["weight"])



# url = "https://api.edamam.com/api/recipes/v2?type=public"
# apiId = "96581904"
# key = "17072af2421f3c49bd3544ed58bb75ab"
# healthLabel = "vegetarian"

# def link_builder(url, apiId, key, healthLabel):
#     return '{}&{}&{}&{}&mealType=Dinner&random=true'.format(url, apiId, key, healthLabel)

# print(link_builder(url, apiId, key, healthLabel))
