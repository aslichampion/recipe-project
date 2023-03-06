from django.test import TestCase
from recipes.models import CurrentRecipes
from django.contrib.auth.models import User


class RecipeViews(TestCase):
    def test_call_view_deny_anonymous(self):
        # Why does the trailing / matter in the URL?
        test_user = User(first_name='Test', last_name='Test', username='Test', password='Test')
        test_user.save()
        test_recipes = CurrentRecipes(user_id=test_user.id, current_week_recipes="test")
        test_recipes.save()
        response = self.client.get('/recipes', follow=True)
        self.assertEqual(response.status_code, 200)
