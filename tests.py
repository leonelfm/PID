from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class SolutionEndpointTest(TestCase):
    def setUp(self):
        self.client = APIClient()


def test_solution_endpoint(self):
    data = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Maquina", "quantity": 5, "price": 56, "status": "completed"}
        ],
        "criterion": "completed"
    }

    response = self.client.post('/api/solution/', data, format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    self.assertIn("result", response.data)
