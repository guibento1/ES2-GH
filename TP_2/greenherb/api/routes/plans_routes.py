from fastapi import APIRouter, Depends, status

from api.controllers import plans_controller
from api.dependencies.auth_deps import get_current_user
from api.models.schemas import PlanCreate, PlanResponse

router = APIRouter(prefix="/plans", tags=["plans"])

@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_plans(user=Depends(get_current_user)):
    return plans_controller.get_plans()

@router.post("", response_model=PlanResponse, status_code=status.HTTP_201_CREATED)
def create_plan(payload: PlanCreate, user=Depends(get_current_user)):
    return plans_controller.post_plan(payload.model_dump())
