import json
from decimal import Decimal
from uuid import UUID

from django.conf import settings
from rest_framework import status
from rest_framework.request import Request

from utils.exceptions import (
    AuthenticationException,
    InventoryAvailabilityException,
    InventoryNotFoundException,
)
from utils.http_client import http_request


def check_inventory(request: Request, inventory_id: UUID):
    """
    This method checks if inventory exists.
    """

    url = f"{settings.MICROSERVICES.get('warehouse')}/inventory/{inventory_id}/"
    response = http_request.get(url=url, headers=request.headers)

    if response.status_code == status.HTTP_404_NOT_FOUND:
        raise InventoryNotFoundException()

    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        raise AuthenticationException()


def exit_inventory_from_warehouse(request: Request, inventory_id: UUID, amount: UUID):
    """
    This method checks if inventory is available and
    if it is inventory will be reduced in warehouse
    """

    request_data = {"inventory": inventory_id, "amount": amount}

    url = f"{settings.MICROSERVICES.get('warehouse')}/inventory/exit/"

    response = http_request.post(url=url, data=request_data, headers=request.headers)

    if response.status_code == status.HTTP_404_NOT_FOUND:
        raise InventoryNotFoundException()

    if response.status_code == status.HTTP_400_BAD_REQUEST:
        raise InventoryAvailabilityException()

    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        raise AuthenticationException()

    return json.loads(response.content.decode("utf-8"))


def convert_uuids_to_strings(data: dict) -> dict:
    for k, v in data.items():
        if isinstance(v, UUID) or isinstance(v, Decimal):
            data[k] = str(v)

    return data
