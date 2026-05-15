from fastapi import HTTPException, status

from app.services.auth_service import (
    AuthInputValidationError,
    TokenValidationError,
    authenticate_user,
    generate_token,
    refresh_token,
    validate_login_payload,
)


def login(credentials):
    try:
        username, password = validate_login_payload(credentials)
        user = authenticate_user(username, password)
    except AuthInputValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password.",
        )

    return {
        "access_token": generate_token(user, token_type="access"),
        "refresh_token": generate_token(user, token_type="refresh"),
        "token_type": "bearer",
    }


def renew_token(payload):
    try:
        token_pair = refresh_token(payload.refresh_token)
    except TokenValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token.",
        ) from error

    if token_pair is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token.",
        )
    return token_pair
