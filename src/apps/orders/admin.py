from django.contrib import admin

from apps.orders.models import Margin, Order

admin.site.register(Order)
admin.site.register(Margin)
