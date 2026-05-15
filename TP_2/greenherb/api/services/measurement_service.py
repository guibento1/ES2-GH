from api.data import memory_store
from api.services.alert_service import classify_alert, create_alert


class MeasurementValidationError(ValueError):
    status_code = 400


def _get_plan_limits(batch):
    """Return plan limits for a batch, or safe defaults if no plan is linked."""
    plan_id = batch.get("plan_id")
    if plan_id:
        plan = memory_store.find_plan_by_id(plan_id)
        if plan and plan.get("temp_max") and plan.get("humidity_min"):
            return {
                "temp_max": plan["temp_max"],
                "humidity_min": plan["humidity_min"],
            }
    # Defaults matching the standard cultivation ranges
    return {"temp_max": 28.0, "humidity_min": 40.0}


def create_measurement(payload):
    """
    Store a measurement and auto-classify any alert against the batch plan limits.
    Returns the measurement record with an optional embedded alert.
    """
    batch_id = payload.get("batch_id")
    temp = payload.get("temp")
    humidity = payload.get("humidity")
    luminosity = payload.get("luminosity")
    sensor_ok = payload.get("sensor_ok", True)

    if any(v is None for v in (batch_id, temp, humidity, luminosity)):
        raise MeasurementValidationError(
            "batch_id, temp, humidity and luminosity are required."
        )

    measurement = memory_store.add_measurement({
        "batch_id": batch_id,
        "temp": temp,
        "humidity": humidity,
        "luminosity": luminosity,
        "sensor_ok": sensor_ok,
    })

    # Auto-classify and persist alert if limits are violated
    batch = memory_store.find_batch_by_id(batch_id)
    alert_record = None
    if batch:
        limits = _get_plan_limits(batch)
        level = classify_alert(temp, humidity, limits, sensor_ok)
        if level:
            alert_record = create_alert({
                "batch_id": batch_id,
                "level": level,
                "temp": temp,
                "humidity": humidity,
            })

    return {**measurement, "alert": alert_record}


def list_measurements():
    return memory_store.list_measurements()
