from django.urls import path

from apps.orders.views import (
    MarginDetailAPIView,
    MarginListAPIView,
    OrderDetailAPIView,
    OrderListAPIView,
)

urlpatterns = [
    path("", OrderListAPIView.as_view(), name="order-list"),
    path("<uuid:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
    path("margin/", MarginListAPIView.as_view(), name="margin-list"),
    path("margin/<uuid:pk>/", MarginDetailAPIView.as_view(), name="margin-detail"),
]
