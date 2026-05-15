from fastapi import APIRouter, status

from api.controllers import batches_controller
from api.models.schemas import BatchCloseRequest, BatchCreate, BatchResponse


router = APIRouter(prefix="/batches", tags=["batches"])


@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_batches():
    return batches_controller.get_batches()


@router.post("", response_model=BatchResponse, status_code=status.HTTP_201_CREATED)
def create_batch(payload: BatchCreate):
    return batches_controller.post_batch(payload.model_dump())


@router.patch("/{batch_id}/close", response_model=BatchResponse, status_code=status.HTTP_200_OK)
def close_batch(batch_id: int, payload: BatchCloseRequest):
    """Fecha o lote: transita estado e calcula produtividade."""
    return batches_controller.patch_close_batch(batch_id, payload.model_dump())
