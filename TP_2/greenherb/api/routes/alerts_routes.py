from fastapi import APIRouter, status

from api.controllers import alerts_controller
from api.models.schemas import AlertResolveRequest, AlertResponse


router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_alerts():
    return alerts_controller.get_alerts()


@router.patch("/{alert_id}", response_model=AlertResponse, status_code=status.HTTP_200_OK)
def resolve_alert(alert_id: int, payload: AlertResolveRequest):
    """Resolve ou ignora um alerta (ignorar exige justificação 10–500 chars)."""
    return alerts_controller.patch_alert(alert_id, payload.model_dump())
