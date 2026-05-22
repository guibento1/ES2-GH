from fastapi import APIRouter, Depends, status

from api.controllers import automation_controller
from api.dependencies.auth_deps import get_current_user
from api.models.schemas import AutomationEvaluateRequest, AutomationEvaluateResponse, AutomationRuleCreate

router = APIRouter(prefix="/automation", tags=["automation"])

@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_automation_rules(user=Depends(get_current_user)):
    return automation_controller.get_automation_rules()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_automation_rule(payload: AutomationRuleCreate, user=Depends(get_current_user)):
    return automation_controller.post_automation_rule(payload.model_dump())

@router.post("/evaluate", response_model=AutomationEvaluateResponse, status_code=status.HTTP_200_OK)
def evaluate_automation(payload: AutomationEvaluateRequest, user=Depends(get_current_user)):
    return automation_controller.post_evaluate(payload.model_dump())
