from fastapi import HTTPException, status

from api.services.user_service import UserValidationError, create_user, list_users


def get_users():
    return {"users": list_users()}


def post_user(payload: dict):
    try:
        return create_user(payload)
    except UserValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
