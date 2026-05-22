# Schemas Pydantic — validação de input (corpo de pedidos) e serialização de output
# (response_model) dos endpoints HTTP.
#
# A persistência fica em `api/data/memory_store.py` (em produção seria SQLAlchemy).
# Os endpoints devem usar SEMPRE estes schemas — nunca os dicionários do store.

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


class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str | None = None
    role: str


class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str | None = None
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
# Batches
# ---------------------------------------------------------------------------

class BatchCreate(BaseModel):
    herb_id: int
    plan_id: int | None = None
    planned_qty: float


class BatchCloseRequest(BaseModel):
    has_losses: bool
    actual_qty: float
    losses: float = 0.0


class BatchResponse(BaseModel):
    id: int
    herb_id: int
    plan_id: int | None = None
    state: str
    planned_qty: float
    actual_qty: float | None = None
    losses: float | None = None
    productivity: float | None = None


# ---------------------------------------------------------------------------
# Measurements
# ---------------------------------------------------------------------------

class MeasurementCreate(BaseModel):
    batch_id: int
    temp: float
    humidity: float
    luminosity: float
    sensor_ok: bool = True


class MeasurementResponse(BaseModel):
    id: int
    batch_id: int
    temp: float
    humidity: float
    luminosity: float
    sensor_ok: bool
    alert: Any | None = None


# ---------------------------------------------------------------------------
# Alerts
# ---------------------------------------------------------------------------

class AlertResolveRequest(BaseModel):
    action: str          # "resolvido" | "ignorado"
    justification: str | None = None


class AlertResponse(BaseModel):
    id: int
    batch_id: int | None = None
    level: str | None = None   # "Aviso" | "Crítico"
    state: str                 # "pendente" | "resolvido" | "ignorado"
    justification: str | None = None


# ---------------------------------------------------------------------------
# Automation
# ---------------------------------------------------------------------------

class AutomationRuleCreate(BaseModel):
    name: str
    mode: str             # "Manual" | "Automático"
    condition: str | None = None


class AutomationEvaluateRequest(BaseModel):
    mode: str
    rule_active: bool
    measurement_recent: bool


class AutomationEvaluateResponse(BaseModel):
    decision: str         # "executada" | "sugerida" | "ignorada"


# ---------------------------------------------------------------------------
# Tasks
# ---------------------------------------------------------------------------

class TaskCreate(BaseModel):
    batch_id: int
    task_type: str                          # "rega" | "fertilização" | "colheita" | "monitorização"
    scheduled_date: str | None = None       # ISO format YYYY-MM-DD


class TaskResponse(BaseModel):
    id: int
    batch_id: int
    task_type: str
    scheduled_date: str | None = None
