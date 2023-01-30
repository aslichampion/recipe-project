from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
from decouple import config
from main.models import User

# Create your views here.

def recipes(request):
    return render(request, 'recipes/recipes.html')


def getRecipe(request):

    # Retrieve a week of recipes from the API
    apiLink = "https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&health=vegetarian&mealType=Dinner&random=true".format(config('API_ID'), config('API_KEY'))
    apiResponse = requests.get(apiLink)
    recipes = json.loads(apiResponse.text)
    
    # Load the JSON recipes into the database, first user hardcoded for now
    currentUser = User.objects.get(pk=1)
    currentUser.current_week_recipes = recipes
    currentUser.save()

    # Loads the correct template and sets the variable name within the template as the 'context'
    template = loader.get_template('recipes/recipes.html')
    context = {
        'weeklyRecipes': currentUser.current_week_recipes,
    }
    return HttpResponse(template.render(context, request))


# url = "https://api.edamam.com/api/recipes/v2?type=public"
# apiId = "96581904"
# key = "17072af2421f3c49bd3544ed58bb75ab"
# healthLabel = "vegetarian"

# def link_builder(url, apiId, key, healthLabel):
#     return '{}&{}&{}&{}&mealType=Dinner&random=true'.format(url, apiId, key, healthLabel)

# print(link_builder(url, apiId, key, healthLabel))
