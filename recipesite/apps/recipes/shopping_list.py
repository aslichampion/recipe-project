### CODE

# Test Origin List
# test_origin_ingredients1 = [
#     {'food':'apple', 'quantity': 100, 'measure': 'grams'},
#     {'food':'banana', 'quantity': 200, 'measure': 'units'},
#     {'food':'banana', 'quantity': 300, 'measure': 'grams'},
#     {'food':'banana', 'quantity': 100, 'measure': 'grams'},
#     {'food':'carrot', 'quantity': 100, 'measure': 'bunch'},
#     {'food':'carrot', 'quantity': 300, 'measure': 'bunch'},
#     {'food':'damson', 'quantity': 200, 'measure': 'grams'},
#     {'food':'damson', 'quantity': 400, 'measure': 'grams'},
#     {'food':'damson', 'quantity': 100, 'measure': 'teaspoons'},
#     {'food':'damson', 'quantity': 300, 'measure': 'cups'},
# ]

def consolidate_ingredients(ingredients):

    # Origin List sorted alphabetically by food then measure
    origin_ingredients = sorted(ingredients, key=lambda d: (d['food'], d['measure']))

    # Destination List (empty)
    destination_ingredients = []
    print(
        'OUTPUT: destination_ingredients: {}'.format(
            destination_ingredients
        )
    )

    # Variables for initial index of first ingredient, index of penultimate ingredient in array, and initial duplicate ingredient
    index = 0
    penultimate_ingredient_index = len(origin_ingredients) - 1
    duplicate_ingredient = origin_ingredients[0]

    # Loop from first to penultimate ingredient
    for i in range(0,penultimate_ingredient_index):

        # Assign first and next ingredients
        first_ingredient = origin_ingredients[index]
        next_ingredient = origin_ingredients[index+1]

        # If ingredient names match
        if first_ingredient['food'] == next_ingredient['food']:

            # Summary of first and next ingredients
            print(
                "TRUE ('food'): {}: {} {} vs {}: {} {}".format(
                    first_ingredient['food'], 
                    first_ingredient['quantity'], 
                    first_ingredient['measure'], 
                    next_ingredient['food'],
                    next_ingredient['quantity'],
                    next_ingredient['measure']
                )
            )

            # If ingredient names and ingredient measures match
            if first_ingredient['measure'] == next_ingredient['measure']:

                # Summary of first and next ingredients
                print(
                    "TRUE ('measure'): {}: {} {} vs {}: {} {}".format(
                        first_ingredient['food'], 
                        first_ingredient['quantity'], 
                        first_ingredient['measure'], 
                        next_ingredient['food'],
                        next_ingredient['quantity'],
                        next_ingredient['measure']
                    )
                )

                # Update duplicate ingredient quantity
                duplicate_ingredient['quantity'] += next_ingredient['quantity']

                # Summary of duplicate ingredient (expect quantity to be updated)
                print(
                    "UPDATE: duplicate_ingredient: {}".format(
                        duplicate_ingredient
                    )
                )
            
            # If ingredient names match and ingredient measures do not match
            else:

                # Summary of first and next ingredients
                print(
                    "FALSE ('measure'): {}: {} {} vs {}: {} {}".format(
                        first_ingredient['food'], 
                        first_ingredient['quantity'], 
                        first_ingredient['measure'], 
                        next_ingredient['food'],
                        next_ingredient['quantity'],
                        next_ingredient['measure']
                    )
                )

                # Add duplicate ingredient to destination ingredients
                destination_ingredients.append(duplicate_ingredient)

                # Update duplicate ingredient to next ingredient
                duplicate_ingredient = next_ingredient

                # Summary of destination ingredients (expect duplicate ingredient to be added)
                print(
                    'ADD: destination_ingredients: {}'.format(
                        destination_ingredients
                    )
                )

            # If final two ingredient names match  
            if index + 1 == penultimate_ingredient_index:

                # Add duplicate ingredient to destination ingredients
                destination_ingredients.append(duplicate_ingredient)

        # If ingredient names do not match
        else:

            # Summary of first and next ingredients
            print(
                "FALSE ('food'): {}: {} vs {}: {}".format(
                    first_ingredient['food'], 
                    first_ingredient['quantity'], 
                    next_ingredient['food'],
                    next_ingredient['quantity']
                )
            )

            # Add duplicate ingredient to destination ingredients
            destination_ingredients.append(duplicate_ingredient)

            # Update duplicate ingredient to next ingredient
            duplicate_ingredient = next_ingredient

            # Summary of destination ingredients (expect duplicate ingredient to be added)
            print(
                'ADD: destination_ingredients: {}'.format(
                    destination_ingredients
                )
            )

        index += 1

    # Final summary of destination ingredients (expect all ingredients consolidated)
    print(
        'OUTPUT: destination_ingredients: {}'.format(
            destination_ingredients
        )
    )

    # Return the consolidated destination ingredients array with added and updated ingredients
    return destination_ingredients



### TESTS

# 1: Test array of ingredient dictionaries
test_origin_ingredients1 = [
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'banana', 'quantity': 200, 'measure': 'units'},
    {'food':'banana', 'quantity': 300, 'measure': 'grams'},
    {'food':'banana', 'quantity': 100, 'measure': 'grams'},
    {'food':'carrot', 'quantity': 100, 'measure': 'bunch'},
    {'food':'carrot', 'quantity': 300, 'measure': 'bunch'},
    {'food':'damson', 'quantity': 200, 'measure': 'grams'},
    {'food':'damson', 'quantity': 400, 'measure': 'grams'},
    {'food':'damson', 'quantity': 100, 'measure': 'teaspoons'},
    {'food':'damson', 'quantity': 300, 'measure': 'cups'},
]
expected_destination_ingredients1 = [
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'banana', 'quantity': 400, 'measure': 'grams'},
    {'food':'banana', 'quantity': 200, 'measure': 'units'},
    {'food':'carrot', 'quantity': 400, 'measure': 'bunch'},
    {'food':'damson', 'quantity': 300, 'measure': 'cups'},
    {'food':'damson', 'quantity': 600, 'measure': 'grams'},
    {'food':'damson', 'quantity': 100, 'measure': 'teaspoons'},
]
def test1_ingredients():
    print("")
    print("*** TEST 1 ***")
    print("")
    assert consolidate_ingredients(test_origin_ingredients1) == expected_destination_ingredients1, "TEST1: Should be array of 7 dictionaries"

# 2. Test array of ingredient dictionaries sorted by food and measure
test_origin_ingredients2_sorted = [
    {'food':'apple', 'quantity': 100, 'measure': 'bag'},
    {'food':'apple', 'quantity': 100, 'measure': 'bag'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'unit'},
    {'food':'apple', 'quantity': 100, 'measure': 'unit'},
    {'food':'apple', 'quantity': 100, 'measure': 'unit'},
]
expected_destination_ingredients2_sorted = [
    {'food':'apple', 'quantity': 200, 'measure': 'bag'},
    {'food':'apple', 'quantity': 500, 'measure': 'grams'},
    {'food':'apple', 'quantity': 300, 'measure': 'unit'},
]
def test2_sorted_ingredients():
    print("")
    print("*** TEST 2 ***")
    print("")
    assert consolidate_ingredients(test_origin_ingredients2_sorted) == expected_destination_ingredients2_sorted, "TEST2: Should be array of 3 dictionaries"

# 3. Test array of ingredient dictionaries unsorted
test_origin_ingredients3_unsorted = [
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'unit'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'bag'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'unit'},
    {'food':'apple', 'quantity': 100, 'measure': 'grams'},
    {'food':'apple', 'quantity': 100, 'measure': 'unit'},
    {'food':'apple', 'quantity': 100, 'measure': 'bag'},
]
expected_destination_ingredients3_sorted = [
    {'food':'apple', 'quantity': 200, 'measure': 'bag'},
    {'food':'apple', 'quantity': 500, 'measure': 'grams'},
    {'food':'apple', 'quantity': 300, 'measure': 'unit'},
]
def test3_unsorted_ingredients():
    print("")
    print("*** TEST 3 ***")
    print("")
    assert consolidate_ingredients(test_origin_ingredients3_unsorted) == expected_destination_ingredients3_sorted, "TEST3: Should be array of 3 dictionaries"


# Run tests
if __name__ == "__main__":
    test1_ingredients()
    test2_sorted_ingredients()
    test3_unsorted_ingredients()
    print("")
    print("TESTS: Everything passed")
    print("")