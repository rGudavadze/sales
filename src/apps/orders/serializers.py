from rest_framework import serializers

from apps.orders.helpers import check_inventory, exit_inventory_from_warehouse
from apps.orders.models import InventoryForSale, Order


class InventoryForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryForSale
        fields = (
            "id",
            "inventory_id",
            "price",
        )
        extra_kwargs = {"id": {"read_only": True}}

    def validate(self, attrs):
        attrs = super().validate(attrs)
        check_inventory(self.context.get("request"), attrs.get("inventory_id"))

        return attrs


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "quantity",
            "inventory",
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "quantity",
            "inventory",
        )
        extra_kwargs = {"id": {"read_only": True}}

    def validate(self, attrs):
        attrs = super().validate(attrs)

        inventory_id = attrs.get("inventory").id
        quantity = attrs.get("quantity")

        exit_data = exit_inventory_from_warehouse(
            self.context.get("request"), inventory_id, quantity
        )

        self.context["cost"] = exit_data.get("cost")

        return attrs
