from django.test import TestCase

# Create your tests here.

class RecipeViews(TestCase):
    def test_call_view_deny_anonymous(self):
        # Why does the trailing / matter in the URL?
        response = self.client.get('/recipes', follow=True)
        self.assertEqual(response.status_code, 200)