from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from apps.customers.models import Customer
from apps.customers.serializer import CustomerSerializer


class CustomerListAPIView(ListCreateAPIView):
    """
    APIView to create customer or list all the customers.
    """

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerRetrieveAPIView(RetrieveAPIView):
    """
    APIView to get specific customer.
    """

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
