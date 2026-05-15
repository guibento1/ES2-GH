from typing import Any

from fastapi import APIRouter, status

from app.controllers import plans_controller


router = APIRouter(prefix="/plans", tags=["plans"])


@router.get("", status_code=status.HTTP_200_OK)
def get_plans():
    return plans_controller.get_plans()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_plan_endpoint(payload: dict[str, Any]):
    return plans_controller.create_plan_endpoint(payload)
