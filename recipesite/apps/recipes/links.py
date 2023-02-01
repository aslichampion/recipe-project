from decouple import config

def link_builder(healthLabel):
    if healthLabel == "":
        formattedLabel = healthLabel
    else:
        formattedLabel = '&health={}'.format(healthLabel)
    return 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}{}&mealType=Dinner&random=true'.format(config('API_ID'), config('API_KEY'), formattedLabel)

print(link_builder("vegetarian"))


label="none" value=""
label="Vegetarian" value="vegetarian"