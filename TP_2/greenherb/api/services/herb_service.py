from app.services.mock_service import create_mock, list_mock


def list_herbs():
    return list_mock("herbs")


def create_herb(payload):
    return create_mock("herbs", payload)

