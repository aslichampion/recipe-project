# Recipe Generator App - Group Final Project


## What does it do?

* The click of one button easily generates a list of recipes from a database of thousands of websites across the web.

* Writes a weekly shopping list for you based on the given recipes. No need to trawl through each recipe's ingredient list manually!

* Tailors the suggestions of future recipes based on your feedback as you continue to use the service.

* Aims to take the choice paralysis out of meal planning whilst giving you an exciting mix of food to cook from around the world!

## How does it do it?

* Currently uses the Edamam API to source recipe content.
* Further details of recommendation engine will be added here as the feature is developed.
* And an explanation of the shopping list generation logic will be added here as that gets developed too.

## How do I run it locally?

This project uses Python and the popular web framework Django 

1. Make sure you have Python installed with `$ python3 -V`
2. Create a Python virtual environment in the root of this repo with `$ python3 -m venv .venv`
3. Activate the virtual environment with `$ source .venv/bin/activate`
4. Install any dependencies with `$ pip3 install -r requirements.txt`
5. Create a file called `.env` in the repo root to set the required keys which are in the repo's `.example.env` file.
6. Move into the Django project directory with `$ cd recipesite`
7. Create a PostgreSQL database locally using the command `$ createdb RECIPE_PROJECT`
8. Ensure you have a user for the PostgreSQL database with permission to create databases. Guidance on adding a users can be found in the resources below.
9. To start the app for the first time, migrate info into the DB with `$ python3 manage.py migrate`
10. Then, and on subsequent runs, start the server with `$ python3 manage.py runserver` which should now be running on localhost:8000.


### Resources:
Edamam Recipe Search API: https://www.edamam.com

Python Virtual Environments: https://frankcorso.dev/setting-up-python-environment-venv-requirements.html

Django Web Framework Documentation: https://docs.djangoproject.com

PostgreSQL Documentation - Creating Users : https://www.postgresql.org/docs/8.0/user-attributes.html
