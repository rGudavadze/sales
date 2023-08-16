from django.db import models

from apps.base.models import BaseModel


class InventoryForSale(BaseModel):
    inventory_id = models.UUIDField(help_text="Inventory UUID")
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Price")


class Order(BaseModel):
    customer = models.UUIDField(help_text="Customer")
    quantity = models.PositiveIntegerField(help_text="Quantity")
    inventory = models.ForeignKey(
        to=InventoryForSale, on_delete=models.CASCADE, help_text="Inventory for sale"
    )
