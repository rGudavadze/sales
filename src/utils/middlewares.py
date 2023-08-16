import json

import jwt
from django.conf import settings
from rest_framework.request import Request

from utils.exceptions import AuthenticationFailed

JWT_TOKEN_TYPE = "Bearer"


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request):
        if request.path in ["/api/schema/swagger-ui/", "/api/schema/"]:
            return self.get_response(request)

        raw_token = request.META.get("HTTP_AUTHORIZATION")

        if not raw_token or not isinstance(raw_token, str):
            return AuthenticationFailed(
                json.dumps({"detail": "Authentication credentials were not provided."})
            )

        parts = raw_token.split()

        if len(parts) == 0 or parts[0] != JWT_TOKEN_TYPE:
            return AuthenticationFailed(
                json.dumps({"detail": "Authentication credentials were not provided."})
            )

        if len(parts) != 2:
            return AuthenticationFailed(
                json.dumps(
                    {"detail": "Authorization header must have Bearer token format."}
                )
            )

        token = parts[1]

        try:
            payload = jwt.decode(
                jwt=token,
                key=settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM],
            )
            user_info = payload

        except jwt.DecodeError:
            return AuthenticationFailed(json.dumps({"detail": "Token is invalid."}))

        except jwt.ExpiredSignatureError:
            return AuthenticationFailed(json.dumps({"detail": "Token has expired."}))

        request.user_info = user_info

        return self.get_response(request)
