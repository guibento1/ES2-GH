from typing import Any

from fastapi import APIRouter, status

from api.controllers import tasks_controller


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", status_code=status.HTTP_200_OK)
def get_tasks():
    return tasks_controller.get_tasks()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_task_endpoint(payload: dict[str, Any]):
    return tasks_controller.create_task_endpoint(payload)
