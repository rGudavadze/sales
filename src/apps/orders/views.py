import json

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.orders.helpers import convert_uuids_to_strings
from apps.orders.models import InventoryForSale, Order
from apps.orders.serializers import (
    InventoryForSaleSerializer,
    OrderCreateSerializer,
    OrderSerializer,
)
from utils.rabbitmq_client import rabbitmq_client


class InventoryForSaleAPIView(ListCreateAPIView):
    """
    APIView to create product that are for sale or list all of them.
    """

    serializer_class = InventoryForSaleSerializer
    queryset = InventoryForSale.objects.all()


class OrderListAPIView(ListCreateAPIView):
    """
    APIView to create order or list all the orders.
    """

    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderSerializer
        return OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        inventory_for_sale = InventoryForSale.objects.filter(
            id=serializer.data.get("inventory")
        ).first()

        cost = serializer.context.get("cost")

        data = {
            "inventory_id": inventory_for_sale.inventory_id,
            "customer_id": serializer.data.get("customer"),
            "revenue": inventory_for_sale.price * serializer.data.get("quantity"),
            "cost": cost,
        }

        data = convert_uuids_to_strings(data)

        rabbitmq_client.send_message(
            exchange="", routing_key="sales_queue", message=json.dumps(data)
        )

        return Response(serializer.data)


class OrderDetailAPIView(RetrieveAPIView):
    """
    APIView to get specific order.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
