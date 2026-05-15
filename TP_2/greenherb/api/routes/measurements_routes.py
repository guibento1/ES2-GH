from typing import Any

from fastapi import APIRouter, status

from app.controllers import measurements_controller


router = APIRouter(prefix="/measurements", tags=["measurements"])


@router.get("", status_code=status.HTTP_200_OK)
def get_measurements():
    return measurements_controller.get_measurements()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_measurement_endpoint(payload: dict[str, Any]):
    return measurements_controller.create_measurement_endpoint(payload)
