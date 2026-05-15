from typing import Any

from fastapi import APIRouter, status

from app.controllers import automation_controller


router = APIRouter(prefix="/automation", tags=["automation"])


@router.get("", status_code=status.HTTP_200_OK)
def get_automation_rules():
    return automation_controller.get_automation_rules()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_automation_rule_endpoint(payload: dict[str, Any]):
    return automation_controller.create_automation_rule_endpoint(payload)
