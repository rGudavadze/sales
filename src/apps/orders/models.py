from django.core.validators import MinValueValidator
from django.db import models

from apps.base.models import BaseModel


class Order(BaseModel):
    customer = models.ForeignKey(
        to="customers.Customer",
        on_delete=models.CASCADE,
        help_text="Customer",
    )
    product_id = models.UUIDField(help_text="Product UUID")
    quantity = models.PositiveIntegerField(help_text="Quantity")
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        help_text="Price",
    )


class Margin(BaseModel):
    country_id = models.UUIDField(help_text="Country UUID")
    percent = models.PositiveIntegerField(
        help_text="Percent",
        validators=[MinValueValidator],
    )
