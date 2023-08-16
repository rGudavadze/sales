from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer


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
