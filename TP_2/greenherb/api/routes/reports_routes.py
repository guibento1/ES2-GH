from typing import Any

from fastapi import APIRouter, status

from api.controllers import reports_controller


router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("", status_code=status.HTTP_200_OK)
def get_reports():
    return reports_controller.get_reports()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_report_endpoint(payload: dict[str, Any]):
    return reports_controller.create_report_endpoint(payload)
