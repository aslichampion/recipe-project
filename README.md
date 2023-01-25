# Recipe Generator App - Group Final Project


## What does it do?

* The click of one button easily generates a list of recipes from a database of thousands of websites across the web.

* Writes a weekly shopping list for you based on the given recipes. No need to trawl through each recipe's ingredient list manually!

* Tailors the suggestions of future recipes based on your feedback as you continue to use the service.

* Aims to take the choice paralysis out of meal planning whilst giving you an exciting mix of food to cook from around the world!

## How does it do it?

* Currently uses the Edamam API to source recipe content.
* talk about recommendation engine stuff here.
* and an explanation of the shopping list generation logic here.

## How do I run it locally?

This project uses Python and the popular web framework Django 

1. Make sure you have Python installed with `$ python3 -V` 
2. Create a Python virtual environment in the root of this repo with `$ python3 -m venv .venv`
3. Activate the virtual environment with `$ source .venv/bin/activate`
4. Install any dependencies with `$ pip3 install -r requirements.txt`
5. Create a .env file in the repo root to set a SECRET_KEY environment variable for Django. The contents of this file should be: `SECRET_KEY={secret key goes here}`. This key will not be used in production.
6. Move into the Django project directory with `$ cd recipesite`
7. To start the app for the first time, migrate info into the DB with `$ python3 manage.py migrate`
8. Then, and on subsequent runs, start the server with `$ python3 manage.py runserver` which should now be running on localhost:8000

### Resources:
https://www.edamam.com

https://frankcorso.dev/setting-up-python-environment-venv-requirements.html

https://docs.djangoproject.com
