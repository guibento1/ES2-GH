from app.services.mock_service import list_mock


def list_audit_logs():
    return list_mock("audit")

