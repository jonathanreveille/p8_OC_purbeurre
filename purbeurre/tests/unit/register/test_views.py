from django.test import TestCase
from django.contrib.auth.models import User


class UsersTestViews(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="Foodlover12", password="testing123321")

    def test_user_profile(self):
        self.client.login(username="Foodlover12", password="testing123321")
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("register/profile.html")
