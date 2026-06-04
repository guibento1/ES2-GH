import pytest

from api.services.plan_service import PlanValidationError, validate_plan


# ---------------------------------------------------------------------------
# Helper: plano regular mínimo válido; aceita overrides por campo
# ---------------------------------------------------------------------------

def _plano(**overrides):
    base = {"type": "regular"}
    base.update(overrides)
    return base


# ---------------------------------------------------------------------------
# TU-39 a TU-43 — Temperatura [18, 28] °C
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, temp, esperado",
    [
        ("TU-39", 17, "erro"),   # VL: abaixo do limite inferior (17 < 18)
        ("TU-40", 29, "erro"),   # VL: acima do limite superior (29 > 28)
        ("TU-41", 18, "ok"),     # VL: limite inferior exacto
        ("TU-42", 28, "ok"),     # VL: limite superior exacto
        ("TU-43", 23, "ok"),     # VL: valor nominal interior
    ],
)
def test_temperatura(test_id, temp, esperado):
    """VL: temp_min no intervalo [18, 28] °C (TU-39 a TU-43)."""
    payload = _plano(temp_min=temp)
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)


# ---------------------------------------------------------------------------
# TU-44 a TU-48 — Humidade relativa [40, 80] %
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, hum, esperado",
    [
        ("TU-44", 39, "erro"),   # VL: abaixo do limite inferior (39 < 40)
        ("TU-45", 81, "erro"),   # VL: acima do limite superior (81 > 80)
        ("TU-46", 40, "ok"),     # VL: limite inferior exacto
        ("TU-47", 80, "ok"),     # VL: limite superior exacto
        ("TU-48", 64, "ok"),     # VL: valor nominal interior
    ],
)
def test_humidade(test_id, hum, esperado):
    """VL: humidity_min no intervalo [40, 80] % (TU-44 a TU-48)."""
    payload = _plano(humidity_min=hum)
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)


# ---------------------------------------------------------------------------
# TU-49 a TU-53 — Luminosidade [5000, 25000] lux
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, lux, esperado",
    [
        ("TU-49",  4999, "erro"),   # VL: abaixo do limite inferior (4999 < 5000)
        ("TU-50", 25001, "erro"),   # VL: acima do limite superior (25001 > 25000)
        ("TU-51",  5000, "ok"),     # VL: limite inferior exacto
        ("TU-52", 25000, "ok"),     # VL: limite superior exacto
        ("TU-53", 15000, "ok"),     # VL: valor nominal interior
    ],
)
def test_luminosidade(test_id, lux, esperado):
    """VL: luminosity_min no intervalo [5000, 25000] lux (TU-49 a TU-53)."""
    payload = _plano(luminosity_min=lux)
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)


# ---------------------------------------------------------------------------
# TU-54 a TU-56 — Plano pontual: exigência de autorização do Responsável Técnico
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, authorized_by, esperado",
    [
        ("TU-54", "responsavel", "ok"),   # PE: autorização presente e válida → aceita
        ("TU-55", None,          "erro"), # PE: chave authorized_by ausente (None) → rejeita
        ("TU-56", "",            "erro"), # PE: authorized_by vazio → rejeita
    ],
)
def test_pontual_autorizacao(test_id, authorized_by, esperado):
    """PE: plano pontual exige authorized_by não vazio (TU-54 a TU-56).
    Regra: sem autorização explícita do Responsável Técnico o plano pontual não pode ser criado."""
    payload = {"type": "pontual", "authorized_by": authorized_by}
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)


# ---------------------------------------------------------------------------
# TU-153 a TU-157 — Duração do ciclo [1, 365] dias
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, dias, esperado",
    [
        ("TU-153",   0, "erro"),   # VL: abaixo do limite inferior (0 < 1)
        ("TU-154",   1, "ok"),     # VL: limite inferior exacto
        ("TU-155",  90, "ok"),     # VL: valor nominal interior
        ("TU-156", 365, "ok"),     # VL: limite superior exacto
        ("TU-157", 366, "erro"),   # VL: acima do limite superior (366 > 365)
    ],
)
def test_duracao_ciclo(test_id, dias, esperado):
    """VL: duration_days no intervalo [1, 365] dias (TU-153 a TU-157)."""
    payload = _plano(duration_days=dias)
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)
