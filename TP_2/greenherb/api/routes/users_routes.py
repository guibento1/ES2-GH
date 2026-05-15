from fastapi import APIRouter, status

from api.controllers import users_controller


router = APIRouter(prefix="/users", tags=["users"])


@router.get("", status_code=status.HTTP_200_OK)
def get_users():
    return users_controller.get_users()
