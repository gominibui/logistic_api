from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Order


class OrderTests(APITestCase):
    def setUp(self):
        self.url = reverse("order-list")
        self.valid_order_data = {
            "description": "Test Order",
            "status": "pending"
        }
        self.invalid_order_data = {
            "description": "",
            "status": "invalid_status"
        }

    def tearDown(self):
        Order.objects.all().delete()

    def test_create_order(self):
        response = self.client.post(self.url, self.valid_order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["description"], self.valid_order_data["description"])
        self.assertEqual(response.data["status"], self.valid_order_data["status"])

    def test_create_order_invalid(self):
        response = self.client.post(self.url, self.invalid_order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("description", response.data)
        self.assertIn("status", response.data)

    def test_get_order_detail(self):
        order = Order.objects.create(description="Test Order", status="pending")
        response = self.client.get(reverse("order-detail", kwargs={"pk": order.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], order.description)
        self.assertEqual(response.data["status"], order.status)

    def test_get_nonexistent_order(self):
        response = self.client.get(reverse("order-detail", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
