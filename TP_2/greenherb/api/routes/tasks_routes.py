from typing import Any

from fastapi import APIRouter, Depends, status

from api.controllers import tasks_controller
from api.dependencies.auth_deps import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("", status_code=status.HTTP_200_OK)
def get_tasks(user=Depends(get_current_user)):
    return tasks_controller.get_tasks()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_task_endpoint(payload: dict[str, Any], user=Depends(get_current_user)):
    return tasks_controller.create_task_endpoint(payload)
