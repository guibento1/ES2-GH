from fastapi import HTTPException, status

from api.services.measurement_service import (
    MeasurementValidationError,
    create_measurement,
    list_measurements,
)


def get_measurements():
    return {"measurements": list_measurements()}


def post_measurement(payload: dict):
    try:
        return create_measurement(payload)
    except MeasurementValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
