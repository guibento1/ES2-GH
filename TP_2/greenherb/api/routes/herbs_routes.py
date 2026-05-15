from fastapi import APIRouter, Body, status

from api.controllers import herbs_controller
from api.models.schemas import HerbCreate, HerbImportResult, HerbResponse


router = APIRouter(prefix="/herbs", tags=["herbs"])


@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_herbs():
    return herbs_controller.get_herbs()


@router.post("", response_model=HerbResponse, status_code=status.HTTP_201_CREATED)
def create_herb(payload: HerbCreate):
    return herbs_controller.post_herb(payload.model_dump())


@router.post(
    "/import",
    response_model=HerbImportResult,
    status_code=status.HTTP_200_OK,
)
def import_herbs(content: str = Body(..., media_type="text/plain")):
    """Import aromatic herbs from a CSV string (name,family,description)."""
    return herbs_controller.post_import_csv(content)
