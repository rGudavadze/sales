from django.db import models

from apps.base.models import BaseModel


class Customer(BaseModel):
    company_id = models.CharField(max_length=128, help_text="Company ID")
    name = models.CharField(max_length=128, help_text="Name")
