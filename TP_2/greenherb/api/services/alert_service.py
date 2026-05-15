from app.services.mock_service import create_mock, list_mock


def list_alerts():
    return list_mock("alerts")


def create_alert(payload):
    return create_mock("alerts", payload)

