from django.test import TestCase

# Create your tests here.

class RecipeViews(TestCase):
    def test_call_view_deny_anonymous(self):
        response = self.client.get('/recipe', follow=True)
        self.assertEqual(response.status_code, 200)