from api.services.automation_service import create_automation_rule, list_automation_rules


def get_automation_rules():
    return list_automation_rules()


def create_automation_rule_endpoint(payload):
    return create_automation_rule(payload)
