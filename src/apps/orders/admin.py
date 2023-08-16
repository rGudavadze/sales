from django.contrib import admin

from apps.orders.models import InventoryForSale, Order

admin.site.register(InventoryForSale)
admin.site.register(Order)
