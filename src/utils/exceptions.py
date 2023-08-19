from django.http import HttpResponse
from rest_framework import status
from rest_framework.exceptions import APIException


class InventoryAvailabilityException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The Inventory is not in sufficient quantity."
    default_code = "insufficient_error"


class InventoryNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Inventory not found."
    default_code = "not_found_error"


class AuthenticationException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Authentication issue."
    default_code = "authentication_error"


class AuthenticationFailed(HttpResponse):
    status_code = 401


class NotAuthenticated(HttpResponse):
    status_code = 401
