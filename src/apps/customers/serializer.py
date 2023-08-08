from rest_framework import serializers

from apps.customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "company_id",
            "name",
        )
