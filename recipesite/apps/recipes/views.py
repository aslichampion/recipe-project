from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
from decouple import config
from recipes.models import CurrentRecipes
from recipes.models import History
from main.models import User
from django.shortcuts import redirect

# Create your views here.

def saveHistory(currentUser, currentWeekRecipes):

    # Loop to input separate recipe details into a user's history
    for i in range(7):
        history = History(user_id=currentUser, 
                          recipe_uri=currentWeekRecipes.current_week_recipes['hits'][i]['recipe']['uri'], 
                          cuisine = currentWeekRecipes.current_week_recipes['hits'][i]['recipe']['cuisineType'][0]
                          )
        history.save()

def getRecipes(request):

    # Get user, later this will come from current session info
    currentUser = User.objects.get(pk=1)

    # Retrieve a week of recipes from the API
    apiLink = "https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&health=vegetarian&mealType=Dinner&random=true".format(config('API_ID'), config('API_KEY'))
    apiResponse = requests.get(apiLink)
    recipes = json.loads(apiResponse.text)
    
    # Load the JSON recipes into the database, first user hardcoded for now
    currentWeekRecipes = CurrentRecipes.objects.get(pk=1)
    currentWeekRecipes.current_week_recipes = recipes
    currentWeekRecipes.save()

    # Adds recipes form current week, into user's history
    saveHistory(currentUser, currentWeekRecipes)

    # Loads the correct template and sets the variable name within the template as the 'context'
    template = loader.get_template('recipes/recipes.html')
    context = {
        'weeklyRecipes': currentWeekRecipes.current_week_recipes,
    }

    # Redirects user back to showRecipe page so as to not overwrite the new recipes on page reload
    return redirect(showRecipes)

def showRecipes(request):

    # Getting current week recipes from database
    currentWeekRecipes = CurrentRecipes.objects.get(pk=1)

    # Loads the correct template and sets the variable name within the template as the 'context'
    template = loader.get_template('recipes/recipes.html')
    context = {
        'weeklyRecipes': currentWeekRecipes.current_week_recipes,
    }
    return HttpResponse(template.render(context, request))

# def toggleLike():

# Testing route, access at recipes/test
# def getRecipeTest(request):


# URL builder skeleton:

# url = "https://api.edamam.com/api/recipes/v2?type=public"
# apiId = "96581904"
# key = "17072af2421f3c49bd3544ed58bb75ab"
# healthLabel = "vegetarian"

# def link_builder(url, apiId, key, healthLabel):
#     return '{}&{}&{}&{}&mealType=Dinner&random=true'.format(url, apiId, key, healthLabel)

# print(link_builder(url, apiId, key, healthLabel))
