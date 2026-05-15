"""
Testes de unidade — Sprint 2
Módulo: api.services.plan_service  (TU-39 a TU-53)

Técnica: Análise de Valores Limite (VL)

Temperatura  [18, 28] °C       → 17✗  18✓  23✓  28✓  29✗
Humidade     [40, 80] %        → 39✗  40✓  64✓  80✓  81✗
Luminosidade [5000, 25000] lux → 4999✗ 5000✓ 15000✓ 25000✓ 25001✗

TU-39  temp_min = 17     → rejeita  (abaixo do limite inferior)   VL
TU-40  temp_min = 29     → rejeita  (acima do limite superior)    VL
TU-41  temp_min = 18     → aceita   (limite inferior exacto)      VL
TU-42  temp_min = 28     → aceita   (limite superior exacto)      VL
TU-43  temp_min = 23     → aceita   (valor nominal interior)      VL
TU-44  humidity_min = 39  → rejeita                               VL
TU-45  humidity_min = 81  → rejeita                               VL
TU-46  humidity_min = 40  → aceita  (limite inferior exacto)      VL
TU-47  humidity_min = 80  → aceita  (limite superior exacto)      VL
TU-48  humidity_min = 64  → aceita  (valor nominal)               VL
TU-49  luminosity_min = 4999  → rejeita  (abaixo do mínimo)       VL
TU-50  luminosity_min = 25001 → rejeita  (acima do máximo)        VL
TU-51  luminosity_min = 5000  → aceita   (limite inferior exacto) VL
TU-52  luminosity_min = 25000 → aceita   (limite superior exacto) VL
TU-53  luminosity_min = 15000 → aceita   (valor nominal interior) VL
"""

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
# TU-81 a TU-83 — Tipo de plano: PE (regular / emergência / inválido)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, plan_type, esperado",
    [
        ("TU-81", "regular",    "ok"),
        ("TU-82", "emergência", "ok"),
        ("TU-83", "invalido",   "erro"),
    ],
)
def test_tipo_plano(test_id, plan_type, esperado):
    """PE: tipo de plano — classes válidas (regular, emergência) e inválida (TU-81 a TU-83)."""
    payload = {"type": plan_type}
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)


# ---------------------------------------------------------------------------
# TU-84 a TU-88 — Duração do ciclo [1, 365] dias: VL
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, days, esperado",
    [
        ("TU-84",   0, "erro"),
        ("TU-85",   1, "ok"),
        ("TU-86",  90, "ok"),
        ("TU-87", 365, "ok"),
        ("TU-88", 366, "erro"),
    ],
)
def test_duracao_ciclo(test_id, days, esperado):
    """VL: duration_days no intervalo [1, 365] dias (TU-84 a TU-88)."""
    payload = _plano(duration_days=days)
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)
