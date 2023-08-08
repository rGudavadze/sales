from rest_framework import serializers

from apps.orders.models import Margin, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "product_id",
            "quantity",
            "price",
        )


class MarginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Margin
        fields = (
            "id",
            "country_id",
            "percent",
        )
