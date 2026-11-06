from fastapi import HTTPException, status

from api.services.task_service import TaskValidationError, create_task, list_tasks


def get_tasks():
    return list_tasks()


def create_task_endpoint(payload):
    try:
        return create_task(payload)
    except TaskValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
