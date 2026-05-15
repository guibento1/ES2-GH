from typing import Any

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str | None
    password: str | None


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    role: str


class MockResourceResponse(BaseModel):
    resource: str
    status: str
    data: Any

