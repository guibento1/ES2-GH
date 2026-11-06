from fastapi import HTTPException, status

from api.services.plan_service import (
    PlanValidationError,
    create_plan,
    list_plans,
)


def get_plans():
    return {"plans": list_plans()}


def post_plan(payload: dict):
    try:
        return create_plan(payload)
    except PlanValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
