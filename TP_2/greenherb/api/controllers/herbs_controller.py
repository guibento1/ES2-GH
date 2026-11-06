from fastapi import HTTPException, status

from api.services.herb_service import (
    HerbValidationError,
    create_herb,
    import_herbs_csv,
    list_herbs,
)


def get_herbs():
    return {"herbs": list_herbs()}


def post_herb(payload: dict):
    try:
        return create_herb(payload)
    except HerbValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


def post_import_csv(content: str):
    try:
        return import_herbs_csv(content)
    except HerbValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
