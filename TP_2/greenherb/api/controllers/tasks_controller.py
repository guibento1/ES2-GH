from api.services.task_service import create_task, list_tasks


def get_tasks():
    return list_tasks()


def create_task_endpoint(payload):
    return create_task(payload)
