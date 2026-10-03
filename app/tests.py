"""
Tests for the app. Run with: python manage.py test
"""

from django.test import TestCase


class PageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
