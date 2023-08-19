import uuid
from decimal import Decimal

import factory
from factory.django import DjangoModelFactory


class InventoryForSaleFactory(DjangoModelFactory):
    inventory_id = factory.Faker("uuid4")
    price = Decimal(5)

    class Meta:
        model = "orders.InventoryForSale"


class OrderFactory(DjangoModelFactory):
    customer = uuid.uuid4()
    quantity = factory.Faker("pyint")
    inventory = factory.SubFactory(InventoryForSaleFactory)

    class Meta:
        model = "orders.Order"
