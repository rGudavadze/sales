from django.http import HttpResponse
from rest_framework import status
from rest_framework.exceptions import APIException


class InventoryAvailabilityException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The Inventory is not in sufficient quantity."
    default_code = "insufficient_error"


class AuthenticationFailed(HttpResponse):
    status_code = 401


class NotAuthenticated(HttpResponse):
    status_code = 401
