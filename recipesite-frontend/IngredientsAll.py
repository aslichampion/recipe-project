import json
from collections import defaultdict

def import_data(filename: str) -> list:
    # Import recipe data from file and return one long list of ingredients
    with open(filename) as f:
        responses = json.load(f)
   
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
    print(dict(measure_dict), types_of_measurements)

recipe_ingredients = import_data("recipes.json")
measurement_dict, types_of_measurements = get_measurements(recipe_ingredients)