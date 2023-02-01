import requests
import json
from collections import defaultdict
from decouple import config
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from recipes.models import CurrentRecipes, History


def saveHistory(user, recipes):

    # Loop to input separate recipe details into a user's history
    for i in range(7):
        history = History(user_id=user.id, 
                          recipe_uri=recipes.current_week_recipes['hits'][i]['recipe']['uri'], 
                          cuisine = recipes.current_week_recipes['hits'][i]['recipe']['cuisineType'][0]
                          )
        history.save()


def getRecipes(request):

    if not request.user.is_authenticated:
        return redirect('/members/login')

    # Get user, later this will come from current session info
    currentUser = request.user

    # Retrieve a week of recipes from the API
    apiLink = "https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&health=vegetarian&mealType=Dinner&random=true".format(config('API_ID'), config('API_KEY'))
    apiResponse = requests.get(apiLink)
    recipes = json.loads(apiResponse.text)
    
    # Load the JSON recipes into the database
    if CurrentRecipes.objects.filter(user_id=currentUser.id).exists():
        currentWeekRecipes = CurrentRecipes.objects.get(user_id=currentUser)
        currentWeekRecipes.current_week_recipes=recipes
        currentWeekRecipes.save()
        # Adds recipes form current week, into user's history
        saveHistory(currentUser, currentWeekRecipes)
    else:
        newWeekRecipes = CurrentRecipes(user_id=currentUser.id, current_week_recipes=recipes)
        newWeekRecipes.save()
        # Adds recipes form first week, into user's history
        saveHistory(currentUser, newWeekRecipes)

    # Loads the correct template and sets the variable name within the template as the 'context'
    template = loader.get_template('recipes/recipes.html')
    context = {
        'weeklyRecipes': currentWeekRecipes.current_week_recipes,
    }

    # Redirects user back to showRecipe page so as to not overwrite the new recipes on page reload
    return redirect(showRecipes)


def showRecipes(request):

    if not request.user.is_authenticated:
       return redirect('/members/login')

    # Getting current week recipes from database
    currentUser = request.user
    currentWeekRecipes = CurrentRecipes.objects.get(user_id = currentUser.id)

    # Shopping list builder
    recipe_ingredients = import_data(currentWeekRecipes.current_week_recipes)
    currentWeekShopping = get_measurements(recipe_ingredients)

    # Loads the correct template and sets the variable name within the template as the 'context'
    template = loader.get_template('recipes/recipes.html')
    context = {
        'weeklyRecipes': currentWeekRecipes.current_week_recipes,
        'weeklyIngredients': currentWeekShopping,
    }
    return HttpResponse(template.render(context, request))


def import_data(jsonOutput: str) -> list:

    # Import recipe data from database and return one long list of ingredients
    responses = jsonOutput
   
    hits = responses["hits"]
    print(f"There are [{len(hits)}] recipes")
    recipe_ingredients_lists = [hit["recipe"]["ingredients"] for hit in hits]
    compact_recipe_ingredients = [
        ingredient
        for ingredients_list in recipe_ingredients_lists
        for ingredient in ingredients_list
    ]
    return compact_recipe_ingredients

def get_measurements(recipe_ingredients: list) -> tuple:

#    Adding all ingredients to a dictionary containing measurements
#    The returned dictionary looks like this in the end with combined quantities from all recipes

#    Also returns a list of all measurements types used by all recipes
   
    measure_dict = defaultdict(dict)
    types_of_measurements = set()  # Used to store all UNIQUE types of measurements
    
    for ingredient in recipe_ingredients:
        food_dict = measure_dict[ingredient["food"]]
    
        quantity = ingredient["quantity"]
        measure = ingredient["measure"]
        types_of_measurements.add(measure)
        
        if measure in food_dict:
            food_dict[measure] += quantity
        else:
            food_dict[measure] = quantity
    
    # print(f"There are [{len(types_of_measurements)}] types of measurements listed below:")
    # print(types_of_measurements)
    return(dict(measure_dict), types_of_measurements)


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
