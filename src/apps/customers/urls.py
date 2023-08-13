from django.urls import path

from apps.customers.views import CustomerListAPIView, CustomerRetrieveAPIView

urlpatterns = [
    path("", CustomerListAPIView.as_view(), name="customer-list"),
    path("<uuid:pk>/", CustomerRetrieveAPIView.as_view(), name="customer-detail"),
]
