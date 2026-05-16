from api.services.mock_service import create_mock, list_mock
from api.utils.date_validator import DateValidationError, validate_date


VALID_TASK_TYPES = {"rega", "fertilização", "colheita", "monitorização"}


class TaskValidationError(ValueError):
    status_code = 400


def validate_task(payload):
    """Validate task creation payload."""
    if payload is None or not isinstance(payload, dict):
        raise TaskValidationError("Payload must be a JSON object.")

    if payload.get("batch_id") is None:
        raise TaskValidationError("batch_id is required.")

    task_type = payload.get("task_type")
    if task_type is None:
        raise TaskValidationError("task_type is required.")
    if task_type not in VALID_TASK_TYPES:
        raise TaskValidationError(
            f"task_type must be one of: {', '.join(sorted(VALID_TASK_TYPES))}."
        )

    try:
        validate_date(payload.get("scheduled_date"))
    except DateValidationError as exc:
        raise TaskValidationError(str(exc)) from exc


def list_tasks():
    return list_mock("tasks")


def create_task(payload):
    validate_task(payload)
    return create_mock("tasks", payload)
