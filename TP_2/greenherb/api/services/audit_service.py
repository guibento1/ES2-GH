from api.services.mock_service import list_mock


AUDITABLE_ACTIONS = {
    "create_batch", "close_batch", "create_plan", "create_herb",
    "resolve_alert", "ignore_alert", "create_task", "create_measurement",
    "create_user", "create_automation_rule",
}


def is_auditable_action(action):
    """Returns True if the action should be recorded in the audit log."""
    if not isinstance(action, str):
        return False
    return action in AUDITABLE_ACTIONS


def list_audit_logs():
    return list_mock("audit")
