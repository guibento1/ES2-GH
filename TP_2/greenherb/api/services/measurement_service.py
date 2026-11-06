from api.data import memory_store
from api.services.alert_service import classify_alert, create_alert


class MeasurementValidationError(ValueError):
    status_code = 400


_DEFAULT_LIMITS = {
    "temp_min": 18.0, "temp_max": 28.0,
    "humidity_min": 40.0, "humidity_max": 80.0,
    "luminosity_min": 5000, "luminosity_max": 25000,
}


def _get_plan_limits(batch):
    plan_id = batch.get("plan_id")
    if plan_id:
        plan = memory_store.find_plan_by_id(plan_id)
        if plan:
            return {
                "temp_min":       plan.get("temp_min",       _DEFAULT_LIMITS["temp_min"]),
                "temp_max":       plan.get("temp_max",       _DEFAULT_LIMITS["temp_max"]),
                "humidity_min":   plan.get("humidity_min",   _DEFAULT_LIMITS["humidity_min"]),
                "humidity_max":   plan.get("humidity_max",   _DEFAULT_LIMITS["humidity_max"]),
                "luminosity_min": plan.get("luminosity_min", _DEFAULT_LIMITS["luminosity_min"]),
                "luminosity_max": plan.get("luminosity_max", _DEFAULT_LIMITS["luminosity_max"]),
            }
    return dict(_DEFAULT_LIMITS)


def create_measurement(payload):
    """Store a measurement and auto-classify any alert against the batch plan limits."""
    batch_id   = payload.get("batch_id")
    temp       = payload.get("temp")
    humidity   = payload.get("humidity")
    luminosity = payload.get("luminosity")
    sensor_ok  = payload.get("sensor_ok", True)

    if any(v is None for v in (batch_id, temp, humidity, luminosity)):
        raise MeasurementValidationError(
            "batch_id, temp, humidity and luminosity are required."
        )
    if not isinstance(sensor_ok, bool):
        raise MeasurementValidationError("sensor_ok must be a boolean (true/false).")

    measurement = memory_store.add_measurement({
        "batch_id": batch_id, "temp": temp, "humidity": humidity,
        "luminosity": luminosity, "sensor_ok": sensor_ok,
    })

    batch = memory_store.find_batch_by_id(batch_id)
    alert_record = None
    if batch:
        limits = _get_plan_limits(batch)
        level = classify_alert(temp, humidity, luminosity, limits, sensor_ok)
        if level:
            alert_record = create_alert({
                "batch_id": batch_id, "level": level,
                "temp": temp, "humidity": humidity,
            })

    return {**measurement, "alert": alert_record}


def list_measurements():
    return memory_store.list_measurements()
