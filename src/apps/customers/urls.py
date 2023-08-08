from django.urls import path

from apps.customers.views import CustomerListAPIView

urlpatterns = [
    path("", CustomerListAPIView.as_view(), name="customer-list"),
    path("<uuid:pk>/", CustomerListAPIView.as_view(), name="customer-detail"),
]
