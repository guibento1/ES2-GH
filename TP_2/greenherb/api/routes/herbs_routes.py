from fastapi import APIRouter, Body, Depends, status

from api.controllers import herbs_controller
from api.dependencies.auth_deps import get_current_user, require_responsavel_or_admin
from api.models.schemas import HerbCreate, HerbImportResult, HerbResponse

router = APIRouter(prefix="/herbs", tags=["herbs"])

@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_herbs(user=Depends(get_current_user)):
    return herbs_controller.get_herbs()

@router.post("", response_model=HerbResponse, status_code=status.HTTP_201_CREATED)
def create_herb(payload: HerbCreate, user=Depends(get_current_user)):
    return herbs_controller.post_herb(payload.model_dump())

@router.post("/import", response_model=HerbImportResult, status_code=status.HTTP_200_OK)
def import_herbs(content: str = Body(..., media_type="text/plain"), user=Depends(require_responsavel_or_admin)):
    return herbs_controller.post_import_csv(content)
