from rest_framework import status

from utils.exceptions import InventoryAvailabilityException


def exit_inventory_from_warehouse(inventory_id, amount):
    """
    This method will check if inventory is available and
        if it is inventory will be reduced in warehouse
    """

    # TODO: http request will be implemented later.

    status_code = 200
    data = {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "inventory": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "amount": "8.1",
        "cost": 5,
    }

    if status_code == status.HTTP_400_BAD_REQUEST:
        raise InventoryAvailabilityException()

    return data
