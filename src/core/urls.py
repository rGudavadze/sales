from django.contrib import admin
from django.urls import include, path

from core.spectacular import urlpatterns as swagger_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include("apps.orders.urls")),
] + swagger_urls
