import uuid

import factory
from factory.django import DjangoModelFactory


class InventoryForSaleFactory(DjangoModelFactory):
    inventory_id = uuid.uuid4()
    price = factory.Faker("pyint")

    class Meta:
        model = "orders.InventoryForSale"


class OrderFactory(DjangoModelFactory):
    customer = uuid.uuid4()
    quantity = factory.Faker("pyint")
    inventory = factory.SubFactory(InventoryForSaleFactory)

    class Meta:
        model = "orders.Order"
