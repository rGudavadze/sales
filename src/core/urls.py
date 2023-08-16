from django.urls import include, path

from core.spectacular import urlpatterns as swagger_urls

urlpatterns = [
    path("orders/", include("apps.orders.urls")),
] + swagger_urls
