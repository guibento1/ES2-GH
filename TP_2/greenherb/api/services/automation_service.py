from app.services.mock_service import create_mock, list_mock


def list_automation_rules():
    return list_mock("automation")


def create_automation_rule(payload):
    return create_mock("automation", payload)

