import requests
import json
from collections import defaultdict
from decouple import config
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import CurrentRecipes, History

MEMBER_LOGIN = "/members/login"


def save_history(user, recipes):
    # Loop to input separate recipe details into a user's history
    for i in range(7):
        history = History(user_id=user.id,
                          recipe_uri=recipes.current_week_recipes['hits'][i]['recipe']['uri'],
                          cuisine=recipes.current_week_recipes['hits'][i]['recipe']['cuisineType'][0]
                          )
        history.save()


def link_builder(health_label):
    if health_label == '':
        formatted_label = health_label
    else:
        formatted_label = '&health={}'.format(health_label)
    return 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}{}' \
           '&mealType=Dinner&random=true'.format(config('API_ID'), config('API_KEY'), formatted_label)


# label="none" value=""
# label="Vegetarian" value="vegetarian"

def get_recipes(request):
    diet = str(request.GET.get('diet'))

    if not request.user.is_authenticated:
        return redirect(MEMBER_LOGIN)

    # Get user, later this will come from the current session info
    current_user = request.user

    api_link = link_builder(diet)
    api_response = requests.get(api_link)
    recipes = json.loads(api_response.text)

    # Load the JSON recipes into the database
    if CurrentRecipes.objects.filter(user_id=current_user.id).exists():
        current_week_recipes = CurrentRecipes.objects.get(user_id=current_user)
        current_week_recipes.current_week_recipes = recipes
        current_week_recipes.save()
        # Adds recipes from current week, into user's history
        save_history(current_user, current_week_recipes)
    else:
        new_week_recipes = CurrentRecipes(user_id=current_user.id, current_week_recipes=recipes)
        new_week_recipes.save()
        # Adds recipes from first week, into user's history
        save_history(current_user, new_week_recipes)

    # Redirects the user back to showRecipe page to not overwrite the new recipes on page reload
    return redirect(show_recipes)


def show_recipes(request):
    if not request.user.is_authenticated:
        return redirect(MEMBER_LOGIN)

    # Getting current week recipes from the database
    current_user = request.user
    sliced_recipes = CurrentRecipes.objects.get(user_id=current_user.id).current_week_recipes["hits"][:7]

    # Loads the correct template and sets the variable name within the template as the 'context'
    template = loader.get_template('recipes/recipes.html')
    context = {
        'slicedRecipes': sliced_recipes,
    }
    return HttpResponse(template.render(context, request))


def shopping_list(request):
    if not request.user.is_authenticated:
        return redirect(MEMBER_LOGIN)

    # Getting current week recipes from the database
    current_user = request.user
    sliced_recipes = CurrentRecipes.objects.get(user_id=current_user.id).current_week_recipes["hits"][:7]

    # Shopping list builder
    current_week_shopping = get_measurements(import_data(sliced_recipes))

    # Loads the correct template and sets the variable name within the template as the 'context'
    template = loader.get_template('recipes/list.html')
    context = {
        'weeklyIngredients': list(current_week_shopping.keys()),
    }
    return HttpResponse(template.render(context, request))


def import_data(hits) -> list:
    # Import recipe data from the database and return one long list of ingredients
    print(f"There are [{len(hits)}] recipes")
    recipe_ingredients_lists = [hit["recipe"]["ingredients"] for hit in hits]
    compact_recipe_ingredients = [
        ingredient
        for ingredients_list in recipe_ingredients_lists
        for ingredient in ingredients_list
    ]
    return compact_recipe_ingredients


def get_measurements(recipe_ingredients: list):
    #    Adding all ingredients to a dictionary containing measurements
    #    The returned dictionary looks like this in the end with combined quantities from all recipes
    #    Also returns a list of all measurement types used by all recipes

    measure_dict = defaultdict(dict)
    types_of_measurements = set()  # Used to store all UNIQUE types of measurements

    for ingredient in recipe_ingredients:
        food_dict = measure_dict[ingredient["food"].title()]

        quantity = ingredient["quantity"]
        measure = ingredient["measure"]
        types_of_measurements.add(measure)

        if measure in food_dict:
            food_dict[measure] += quantity
        else:
            food_dict[measure] = quantity
    return dict(measure_dict)
