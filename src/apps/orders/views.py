from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)

from apps.orders.models import Margin, Order
from apps.orders.serializers import MarginSerializer, OrderSerializer


class OrderListAPIView(ListCreateAPIView):
    """
    APIView to create order or list all the orders.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailAPIView(RetrieveAPIView):
    """
    APIView to get specific order.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class MarginListAPIView(ListCreateAPIView):
    """
    APIView to create margin or list all the margins.
    """

    serializer_class = MarginSerializer
    queryset = Margin.objects.all()


class MarginDetailAPIView(RetrieveUpdateAPIView):
    """
    APIView to get or update specific margin.
    """

    serializer_class = MarginSerializer
    queryset = Margin.objects.all()
    http_method_names = ("get", "patch")
