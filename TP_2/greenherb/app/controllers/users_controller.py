from app.services.user_service import list_users


def get_users():
    return {"resource": "users", "status": "mock", "data": list_users()}
