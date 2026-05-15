from api.services.measurement_service import create_measurement, list_measurements


def get_measurements():
    return list_measurements()


def create_measurement_endpoint(payload):
    return create_measurement(payload)
