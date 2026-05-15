from app.services.mock_service import create_mock, list_mock


def list_plans():
    return list_mock("plans")


def create_plan(payload):
    return create_mock("plans", payload)

