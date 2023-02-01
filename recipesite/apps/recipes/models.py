from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# https://docs.djangoproject.com/en/4.1/intro/tutorial02/

class CurrentRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_week_recipes = models.JSONField()

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_uri = models.CharField(max_length=200)
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)
    cuisine = models.CharField(max_length=50)