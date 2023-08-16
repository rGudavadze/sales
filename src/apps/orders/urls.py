from django.urls import path

from apps.orders.views import OrderDetailAPIView, OrderListAPIView

urlpatterns = [
    path("", OrderListAPIView.as_view(), name="order-list"),
    path("<uuid:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
]
