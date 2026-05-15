from fastapi import APIRouter, status

from api.controllers import automation_controller
from api.models.schemas import AutomationEvaluateRequest, AutomationEvaluateResponse, AutomationRuleCreate


router = APIRouter(prefix="/automation", tags=["automation"])


@router.get("", response_model=dict, status_code=status.HTTP_200_OK)
def get_automation_rules():
    return automation_controller.get_automation_rules()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_automation_rule(payload: AutomationRuleCreate):
    return automation_controller.post_automation_rule(payload.model_dump())


@router.post("/evaluate", response_model=AutomationEvaluateResponse, status_code=status.HTTP_200_OK)
def evaluate_automation(payload: AutomationEvaluateRequest):
    """Avalia uma regra de automação e devolve a decisão: executada | sugerida | ignorada."""
    return automation_controller.post_evaluate(payload.model_dump())
