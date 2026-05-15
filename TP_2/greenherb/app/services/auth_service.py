from datetime import datetime, timedelta, timezone
import hmac
import os
from uuid import uuid4

import jwt

from app.data import memory_store


SECRET_KEY = os.getenv(
    "GREENHERB_JWT_SECRET",
    "greenherb-sprint1-secret-with-strong-hs256-length",
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24
MAX_CREDENTIAL_LENGTH = 128
ALLOWED_CREDENTIAL_CHARS = set(
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "._-"
)


class AuthInputValidationError(ValueError):
    """Raised when authentication input is malformed."""

    status_code = 400


class TokenValidationError(ValueError):
    """Raised when a JWT cannot be validated."""


def _validate_credential(field_name, value):
    if value is None:
        raise AuthInputValidationError(f"{field_name} cannot be null.")
    if not isinstance(value, str):
        raise AuthInputValidationError(f"{field_name} must be a string.")
    if value == "" or value.strip() == "":
        raise AuthInputValidationError(f"{field_name} cannot be empty.")
    if len(value) > MAX_CREDENTIAL_LENGTH:
        raise AuthInputValidationError(f"{field_name} is too long.")
    if any(character not in ALLOWED_CREDENTIAL_CHARS for character in value):
        raise AuthInputValidationError(f"{field_name} contains invalid characters.")


def validate_login_payload(payload):
    """Validate raw login request data before authentication."""
    if payload is None or not isinstance(payload, dict):
        raise AuthInputValidationError("Request body must be a JSON object.")

    expected_fields = {"username", "password"}
    received_fields = set(payload.keys())
    if received_fields != expected_fields:
        raise AuthInputValidationError("Request body must contain only username and password.")

    username = payload["username"]
    password = payload["password"]
    _validate_credential("username", username)
    _validate_credential("password", password)
    return username, password


def authenticate_user(username, password):
    """Authenticate a user against the in-memory predefined users."""
    _validate_credential("username", username)
    _validate_credential("password", password)

    user = memory_store.find_user_by_username(username)
    if user is None or not hmac.compare_digest(
        str(password), user["password"]
    ):
        return None

    return memory_store.public_user(user)


def generate_token(user, token_type="access"):
    """Generate a JWT for an authenticated user."""
    if user is None:
        raise ValueError("Cannot generate a token without a user.")
    if token_type not in {"access", "refresh"}:
        raise ValueError("token_type must be 'access' or 'refresh'.")

    now = datetime.now(timezone.utc)
    expiration_minutes = (
        ACCESS_TOKEN_EXPIRE_MINUTES
        if token_type == "access"
        else REFRESH_TOKEN_EXPIRE_MINUTES
    )
    expires_at = now + timedelta(minutes=expiration_minutes)
    jti = str(uuid4())
    payload = {
        "sub": user["username"],
        "id": user["id"],
        "username": user["username"],
        "user_id": user["id"],
        "role": user["role"],
        "type": token_type,
        "iat": now,
        "exp": expires_at,
        "jti": jti,
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    if token_type == "refresh":
        memory_store.REFRESH_TOKENS[jti] = user["username"]
    return token


def decode_token(token, expected_type=None):
    """Decode and validate a JWT, returning its payload."""
    if token is None or not isinstance(token, str) or token.strip() == "":
        raise TokenValidationError("Invalid token.")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError as error:
        raise TokenValidationError("Invalid token.") from error

    if expected_type is not None and payload.get("type") != expected_type:
        raise TokenValidationError("Invalid token type.")
    return payload


def refresh_token(refresh_token_value):
    """Issue a new token pair from a valid refresh token."""
    payload = decode_token(refresh_token_value, expected_type="refresh")
    if payload is None:
        return None

    stored_username = memory_store.REFRESH_TOKENS.get(payload.get("jti"))
    if stored_username != payload.get("sub"):
        return None

    user = memory_store.find_user_by_username(payload["sub"])
    public_user = memory_store.public_user(user)
    if public_user is None:
        return None

    return {
        "access_token": generate_token(public_user, token_type="access"),
        "refresh_token": generate_token(public_user, token_type="refresh"),
        "token_type": "bearer",
    }
