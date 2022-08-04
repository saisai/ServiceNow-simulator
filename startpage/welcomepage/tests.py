from django.test import TestCase


class URLTests(TestCase):
    def test_test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
