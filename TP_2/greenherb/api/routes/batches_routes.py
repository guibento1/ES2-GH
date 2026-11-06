from fastapi import APIRouter, Depends, status

from api.controllers import batches_controller
from api.dependencies.auth_deps import get_current_user
from api.models.schemas import BatchCloseRequest, BatchCreate, BatchResponse

router = APIRouter(prefix="/batches", tags=["batches"])

@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_batches(user=Depends(get_current_user)):
    return batches_controller.get_batches()

@router.post("", response_model=BatchResponse, status_code=status.HTTP_201_CREATED)
def create_batch(payload: BatchCreate, user=Depends(get_current_user)):
    return batches_controller.post_batch(payload.model_dump())

@router.patch("/{batch_id}/close", response_model=BatchResponse, status_code=status.HTTP_200_OK)
def close_batch(batch_id: int, payload: BatchCloseRequest, user=Depends(get_current_user)):
    return batches_controller.patch_close_batch(batch_id, payload.model_dump())
