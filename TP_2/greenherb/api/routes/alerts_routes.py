from typing import Any

from fastapi import APIRouter, status

from api.controllers import alerts_controller


router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("", status_code=status.HTTP_200_OK)
def get_alerts():
    return alerts_controller.get_alerts()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_alert_endpoint(payload: dict[str, Any]):
    return alerts_controller.create_alert_endpoint(payload)
