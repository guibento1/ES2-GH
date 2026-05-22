from fastapi import APIRouter, Depends, status

from api.controllers import measurements_controller
from api.dependencies.auth_deps import get_current_user
from api.models.schemas import MeasurementCreate, MeasurementResponse

router = APIRouter(prefix="/measurements", tags=["measurements"])

@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_measurements(user=Depends(get_current_user)):
    return measurements_controller.get_measurements()

@router.post("", response_model=MeasurementResponse, status_code=status.HTTP_201_CREATED)
def create_measurement(payload: MeasurementCreate, user=Depends(get_current_user)):
    return measurements_controller.post_measurement(payload.model_dump())
