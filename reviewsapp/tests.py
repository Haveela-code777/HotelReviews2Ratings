from django.test import TestCase
from rest_framework import status

# Create your tests here.
class ReviwTestCase(TestCase):
    def test_review_list(self):
        self.review_list_url = "/reviews/list/"
        response = self.client.get(self.review_list_url,{'hotel_id':2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)