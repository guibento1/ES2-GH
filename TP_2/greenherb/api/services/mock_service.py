def list_mock(resource):
    return {
        "resource": resource,
        "status": "mock",
        "data": [],
    }


def create_mock(resource, payload):
    return {
        "resource": resource,
        "status": "created",
        "data": payload,
    }

