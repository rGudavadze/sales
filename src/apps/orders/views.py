from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.orders.models import InventoryForSale, Order
from apps.orders.serializers import (
    InventoryForSaleSerializer,
    OrderCreateSerializer,
    OrderSerializer,
)


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
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # cost = serializer.context.get("cost")
        # TODO: insert into accounting

        return Response(serializer.data)


class OrderDetailAPIView(RetrieveAPIView):
    """
    APIView to get specific order.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
