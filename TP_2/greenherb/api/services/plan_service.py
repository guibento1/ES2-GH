from api.data import memory_store


PLAN_TYPES = {"regular", "emergência", "pontual"}

TEMP_MIN = 18.0
TEMP_MAX = 28.0
HUMIDITY_MIN = 40.0
HUMIDITY_MAX = 80.0
LUMINOSITY_MIN = 5000
LUMINOSITY_MAX = 25000
DURATION_MIN = 1
DURATION_MAX = 365


class PlanValidationError(ValueError):
    """Raised when plan creation data is invalid."""
    status_code = 400


def _check_numeric_range(field, value, low, high):
    """Raise PlanValidationError if value is outside [low, high]."""
    if value is None:
        return
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise PlanValidationError(f"{field} must be a number.")
    if value < low or value > high:
        raise PlanValidationError(
            f"{field} must be between {low} and {high}; got {value}."
        )


def validate_plan(payload):
    """
    Validate plan creation payload.
    Raises PlanValidationError describing the first constraint violated.
    Rules enforced:
      - type in {regular, emergência, pontual}
      - pontual requires a non-empty authorized_by
      - temp_min/max in [18, 28] °C; max >= min
      - humidity_min/max in [40, 80] %; max >= min
      - luminosity_min/max in [5000, 25000] lux; max >= min
      - duration_days in [1, 365]
    """
    if payload is None or not isinstance(payload, dict):
        raise PlanValidationError("Payload must be a JSON object.")

    plan_type = payload.get("type")
    if plan_type not in PLAN_TYPES:
        raise PlanValidationError(
            f"type must be one of: {', '.join(sorted(PLAN_TYPES))}."
        )

    if plan_type == "pontual":
        authorized_by = payload.get("authorized_by")
        if not authorized_by or not isinstance(authorized_by, str) or not authorized_by.strip():
            raise PlanValidationError(
                "authorized_by is required for plano pontual."
            )

    temp_min = payload.get("temp_min")
    temp_max = payload.get("temp_max")
    _check_numeric_range("temp_min", temp_min, TEMP_MIN, TEMP_MAX)
    _check_numeric_range("temp_max", temp_max, TEMP_MIN, TEMP_MAX)
    if temp_min is not None and temp_max is not None and temp_max < temp_min:
        raise PlanValidationError("temp_max must be >= temp_min.")

    humidity_min = payload.get("humidity_min")
    humidity_max = payload.get("humidity_max")
    _check_numeric_range("humidity_min", humidity_min, HUMIDITY_MIN, HUMIDITY_MAX)
    _check_numeric_range("humidity_max", humidity_max, HUMIDITY_MIN, HUMIDITY_MAX)
    if humidity_min is not None and humidity_max is not None and humidity_max < humidity_min:
        raise PlanValidationError("humidity_max must be >= humidity_min.")

    lux_min = payload.get("luminosity_min")
    lux_max = payload.get("luminosity_max")
    _check_numeric_range("luminosity_min", lux_min, LUMINOSITY_MIN, LUMINOSITY_MAX)
    _check_numeric_range("luminosity_max", lux_max, LUMINOSITY_MIN, LUMINOSITY_MAX)
    if lux_min is not None and lux_max is not None and lux_max < lux_min:
        raise PlanValidationError("luminosity_max must be >= luminosity_min.")

    duration = payload.get("duration_days")
    _check_numeric_range("duration_days", duration, DURATION_MIN, DURATION_MAX)


def list_plans():
    return memory_store.list_plans()


def create_plan(payload):
    validate_plan(payload)
    return memory_store.add_plan(payload)
