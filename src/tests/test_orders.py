import os
import uuid
from unittest.mock import patch

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from apps.orders.factories import InventoryForSaleFactory, OrderFactory
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from utils.logger import logger
from utils.rabbitmq_client import rabbitmq_client


class TestOrder(APITestCase):
    def setUp(self):
        self.client = APIClient(headers={"Authorization": os.environ.get("TEST_TOKEN")})
        self.inventory_for_sale = InventoryForSaleFactory.create()
        self.order = OrderFactory.create()
        self.body = {
            "customer": uuid.uuid4(),
            "quantity": 10,
            "inventory": self.inventory_for_sale.id,
        }

    @patch.object(rabbitmq_client, "send_message")
    @patch.object(logger, "info")
    @patch("apps.orders.serializers.exit_inventory_from_warehouse")
    def test_create_order(self, mock_exit, mock_logger, mock_rabbit):
        mock_exit.return_value = {
            "id": uuid.uuid4(),
            "inventory": self.inventory_for_sale.id,
            "amount": 10,
            "cost": 100,
        }
        response = self.client.post(reverse("order-list"), data=self.body)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("inventory"), self.inventory_for_sale.id)

    @patch("apps.orders.serializers.exit_inventory_from_warehouse")
    def test_create_order_serializer(self, mock_exit):
        mock_exit.return_value = {
            "id": uuid.uuid4(),
            "inventory": self.inventory_for_sale.id,
            "amount": 10,
            "cost": 100,
        }

        serializer = OrderSerializer(data=self.body)
        self.assertTrue(serializer.is_valid(raise_exception=True))

        serializer.save()

        self.assertEqual(Order.objects.count(), 2)

    def test_get_orders_list(self):
        self.orders = OrderFactory.create_batch(5)
        response = self.client.get(reverse("order-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_get_order_detail(self):
        response = self.client.get(reverse("order-detail", kwargs={"pk": self.order.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_not_found(self):
        response = self.client.get(reverse("order-detail", kwargs={"pk": uuid.uuid4()}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
