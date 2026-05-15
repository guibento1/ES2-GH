from fastapi import APIRouter, status

from api.controllers import measurements_controller
from api.models.schemas import MeasurementCreate, MeasurementResponse


router = APIRouter(prefix="/measurements", tags=["measurements"])


@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_measurements():
    return measurements_controller.get_measurements()


@router.post("", response_model=MeasurementResponse, status_code=status.HTTP_201_CREATED)
def create_measurement(payload: MeasurementCreate):
    """Regista uma medição e classifica automaticamente um alerta se os limites forem violados."""
    return measurements_controller.post_measurement(payload.model_dump())
