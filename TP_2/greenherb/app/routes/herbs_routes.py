from typing import Any

from fastapi import APIRouter, status

from app.controllers import herbs_controller


router = APIRouter(prefix="/herbs", tags=["herbs"])


@router.get("", status_code=status.HTTP_200_OK)
def get_herbs():
    return herbs_controller.get_herbs()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_herb_endpoint(payload: dict[str, Any]):
    return herbs_controller.create_herb_endpoint(payload)
