from django.test import TestCase


class ProjectViewsTest(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)