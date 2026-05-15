from typing import Any

from fastapi import APIRouter, Body, status

from app.controllers import auth_controller
from app.models.schemas import RefreshTokenRequest, TokenResponse


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(credentials: Any = Body(default=None)):
    return auth_controller.login(credentials)


@router.post("/refresh", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def renew_token(payload: RefreshTokenRequest):
    return auth_controller.renew_token(payload)
