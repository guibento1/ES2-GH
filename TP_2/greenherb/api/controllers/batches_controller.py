from api.services.batch_service import create_batch, list_batches


def get_batches():
    return list_batches()


def create_batch_endpoint(payload):
    return create_batch(payload)
