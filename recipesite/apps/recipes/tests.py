from django.test import TestCase
from main.models import User
from recipes.models import CurrentRecipes

# Create your tests here.

class RecipeViews(TestCase):
    def test_call_view_deny_anonymous(self):
        # Why does the trailing / matter in the URL?
        testUser = User(first_name='Test', last_name='Test', username='Test', password='Test')
        testUser.save()
        testRecipes = CurrentRecipes(user_id=testUser, current_week_recipes="test")
        testRecipes.save()
        response = self.client.get('/recipes', follow=True)
        self.assertEqual(response.status_code, 200)

# class Debugging(TestCase):
#     def test_get_recipes(self):
#         response = self.client.get('/test', follow=True)
#         self.assertEqual(response.status_code, 200)