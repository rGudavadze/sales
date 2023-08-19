import os
import uuid
from unittest.mock import patch

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from apps.orders.factories import InventoryForSaleFactory


class TestInventoryForSale(APITestCase):
    def setUp(self):
        self.client = APIClient(headers={"Authorization": os.environ.get("TEST_TOKEN")})
        self.inventory_for_sale = InventoryForSaleFactory.create()
        self.body = {
            "inventory_id": uuid.uuid4(),
            "price": 10,
        }

    @patch("apps.orders.serializers.check_inventory")
    def test_create_inventory_for_sale(self, mock_check):
        response = self.client.post(reverse("for-sale"), data=self.body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_inventory_for_sale_list(self):
        self.inventory_for_sale = InventoryForSaleFactory.create_batch(5)
        response = self.client.get(reverse("for-sale"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)
