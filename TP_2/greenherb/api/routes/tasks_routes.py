from fastapi import APIRouter, Depends, status

from api.controllers import tasks_controller
from api.dependencies.auth_deps import get_current_user
from api.models.schemas import TaskCreate, TaskResponse


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", status_code=status.HTTP_200_OK)
def get_tasks(user=Depends(get_current_user)):
    return tasks_controller.get_tasks()


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, user=Depends(get_current_user)):
    return tasks_controller.create_task_endpoint(payload.model_dump())
