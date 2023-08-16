from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsAuthenticated(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(request.user_info) and isinstance(request.user_info, dict)
