from typing import Any

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Herbs
# ---------------------------------------------------------------------------

class HerbCreate(BaseModel):
    name: str
    family: str | None = None
    description: str | None = None


class HerbResponse(BaseModel):
    id: int
    name: str
    family: str | None = None
    description: str | None = None


class HerbImportResult(BaseModel):
    imported: int
    partial: int
    failed: int
    valid: list[Any]
    partial_rows: list[Any]
    invalid: list[Any]


# ---------------------------------------------------------------------------
# Plans
# ---------------------------------------------------------------------------

class PlanCreate(BaseModel):
    type: str
    authorized_by: str | None = None
    temp_min: float | None = None
    temp_max: float | None = None
    humidity_min: float | None = None
    humidity_max: float | None = None
    luminosity_min: int | None = None
    luminosity_max: int | None = None
    duration_days: int | None = None


class PlanResponse(BaseModel):
    id: int
    type: str
    authorized_by: str | None = None
    temp_min: float | None = None
    temp_max: float | None = None
    humidity_min: float | None = None
    humidity_max: float | None = None
    luminosity_min: int | None = None
    luminosity_max: int | None = None
    duration_days: int | None = None


# ---------------------------------------------------------------------------
# Legacy mock response (kept for other endpoints still scaffolded)
# ---------------------------------------------------------------------------

class MockResourceResponse(BaseModel):
    resource: str
    status: str
    data: Any
