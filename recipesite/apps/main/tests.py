from django.test import TestCase

# Create your tests here.

class UserModel(TestCase):
    def test_weekly_json(self):
        # This test needs to be updated to test the model
        response = self.client.get('/recipes/new', follow=True)
        self.assertEqual(response.status_code, 200)