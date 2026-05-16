import pytest

from api.services.task_service import TaskValidationError, validate_task


# ---------------------------------------------------------------------------
# TU-82 a TU-86 — PE: tipo de tarefa
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, task_type, esperado",
    [
        ("TU-82", "rega",           "ok"),    # PE: classe válida
        ("TU-83", "fertilização",   "ok"),    # PE: classe válida
        ("TU-84", "colheita",       "ok"),    # PE: classe válida
        ("TU-85", "monitorização",  "ok"),    # PE: classe válida
        ("TU-86", "outro",          "erro"),  # PE: classe inválida
    ],
)
def test_task_type(test_id, task_type, esperado):
    """PE: validate_task — tipos válidos (rega, fertilização, colheita, monitorização) e inválido (TU-82 a TU-86)."""
    payload = {"batch_id": 1, "task_type": task_type}
    if esperado == "erro":
        with pytest.raises(TaskValidationError):
            validate_task(payload)
    else:
        validate_task(payload)


# ---------------------------------------------------------------------------
# TU-87 a TU-89 — PE: campos obrigatórios e data
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, payload, esperado",
    [
        ("TU-87", {"task_type": "rega"},                           "erro"),  # PE: batch_id em falta
        ("TU-88", {"batch_id": 1},                                 "erro"),  # PE: task_type em falta
        ("TU-89", {"batch_id": 1, "task_type": "rega",
                   "scheduled_date": "16-05-2026"},                "erro"),  # PE: data em formato inválido
    ],
)
def test_task_campos_obrigatorios(test_id, payload, esperado):
    """PE: validate_task — campos obrigatórios e validação de data (TU-87 a TU-89)."""
    with pytest.raises(TaskValidationError):
        validate_task(payload)
