from app.services.herb_service import create_herb, list_herbs


def get_herbs():
    return list_herbs()


def create_herb_endpoint(payload):
    return create_herb(payload)
