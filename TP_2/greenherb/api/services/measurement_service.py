from api.services.mock_service import create_mock, list_mock


def list_measurements():
    return list_mock("measurements")


def create_measurement(payload):
    return create_mock("measurements", payload)

