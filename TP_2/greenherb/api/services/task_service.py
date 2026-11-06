from api.utils.date_validator import DateValidationError, validate_date


VALID_TASK_TYPES = {"rega", "fertilização", "colheita", "monitorização"}


class TaskValidationError(ValueError):
    status_code = 400


_TASKS = []
_next_task_id = 1


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
    return list(_TASKS)


def create_task(payload):
    global _next_task_id
    validate_task(payload)
    task = {
        "id":             _next_task_id,
        "batch_id":       payload["batch_id"],
        "task_type":      payload["task_type"],
        "scheduled_date": payload.get("scheduled_date"),
    }
    _next_task_id += 1
    _TASKS.append(task)
    return dict(task)
