from app.services.plan_service import create_plan, list_plans


def get_plans():
    return list_plans()


def create_plan_endpoint(payload):
    return create_plan(payload)
