from typing import Any

from fastapi import APIRouter, status

from api.controllers import batches_controller


router = APIRouter(prefix="/batches", tags=["batches"])


@router.get("", status_code=status.HTTP_200_OK)
def get_batches():
    return batches_controller.get_batches()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_batch_endpoint(payload: dict[str, Any]):
    return batches_controller.create_batch_endpoint(payload)
