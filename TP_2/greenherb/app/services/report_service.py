from app.services.mock_service import create_mock, list_mock


def list_reports():
    return list_mock("reports")


def create_report(payload):
    return create_mock("reports", payload)

