from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from orders.models import Order


class OrderTests(APITestCase):
    def setUp(self):
        self.url = reverse('order-list-create')
        self.order_data = {
            "description": "Test Order 1",
            "status": "pending"
        }

    def test_create_order(self):
        response = self.client.post(self.url, self.order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["description"], self.order_data["description"])
        self.assertEqual(response.data["status"], self.order_data["status"])

    def test_create_order_invalid(self):
        invalid_data = {
            "description": "",
            "status": "invalid_status"
        }
        response = self.client.post(self.url, invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_orders(self):
        Order.objects.create(description="Order 1", status="pending")
        Order.objects.create(description="Order 2", status="completed")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_order_detail(self):
        order = Order.objects.create(description="Order for details", status="in_progress")
        response = self.client.get(reverse('order-detail', kwargs={'pk': order.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], order.description)
        self.assertEqual(response.data["status"], order.status)

    def test_delete_order(self):
        order = Order.objects.create(description="Order to delete", status="completed")
        response = self.client.delete(reverse('order-detail', kwargs={'pk': order.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
