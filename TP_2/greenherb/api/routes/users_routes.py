from fastapi import APIRouter, Depends, status

from api.controllers import users_controller
from api.dependencies.auth_deps import get_current_user, require_admin
from api.models.schemas import UserCreate, UserResponse


router = APIRouter(prefix="/users", tags=["users"])


@router.get("", status_code=status.HTTP_200_OK)
def get_users(user=Depends(get_current_user)):
    return users_controller.get_users()


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, user=Depends(require_admin)):
    return users_controller.post_user(payload.model_dump())
