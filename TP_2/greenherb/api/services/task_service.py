from api.services.mock_service import create_mock, list_mock


def list_tasks():
    return list_mock("tasks")


def create_task(payload):
    return create_mock("tasks", payload)

