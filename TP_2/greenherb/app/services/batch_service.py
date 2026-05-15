from app.services.mock_service import create_mock, list_mock


def list_batches():
    return list_mock("batches")


def create_batch(payload):
    return create_mock("batches", payload)

