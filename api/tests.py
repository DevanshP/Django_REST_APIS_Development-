from django.test import TestCase
from rest_framework.test import APIClient


class BlogPaginationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_blogs_endpoint_returns_paginated_metadata(self):
        response = self.client.get('/api/v1/blogs/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('results', response.data)
