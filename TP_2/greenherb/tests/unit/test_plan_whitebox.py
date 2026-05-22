"""
Sprint 5 — Cobertura de Condições Múltiplas (MC/DC)
Módulo: api.services.plan_service.validate_plan

Expressão lógica da decisão composta:
  resultado = C1 AND C4 AND C5 AND C6 AND (NOT C2 OR C3)

Condições atómicas:
  C1: plan["type"] in {"regular", "emergência", "pontual"}
  C2: plan["type"] == "pontual"
  C3: plan.get("authorized_by") é não-vazio
  C4: temp_min in [18, 28] °C          (None ≡ não avaliado = OK)
  C5: humidity_min in [40, 80] %       (None ≡ não avaliado = OK)
  C6: luminosity_min in [5000, 25000]  (None ≡ não avaliado = OK)

Tabela MC/DC (subconjunto mínimo — 7 casos cobrem 6 condições):

  ID     type       authorized_by  temp_min  hum_min  lux_min  C1  C2  C3  C4  C5  C6  Resultado  Pair
  TU-152 regular    —              23        60       15000    T   F   —   T   T   T   Válido     base
  TU-153 invalido   —              23        60       15000    F   F   —   T   T   T   Erro       C1↕
  TU-154 regular    —              17        60       15000    T   F   —   F   T   T   Erro       C4↕
  TU-155 regular    —              23        35       15000    T   F   —   T   F   T   Erro       C5↕
  TU-156 regular    —              23        60       4000     T   F   —   T   T   F   Erro       C6↕
  TU-157 pontual    None           23        60       15000    T   T   F   T   T   T   Erro       C2↕ C3↕
  TU-158 pontual    "responsavel"  23        60       15000    T   T   T   T   T   T   Válido     C3↕

Pares MC/DC:
  C1: TU-152 (C1=T → Válido) vs TU-153 (C1=F → Erro)             — apenas C1 muda
  C4: TU-152 (C4=T → Válido) vs TU-154 (C4=F → Erro)             — apenas C4 muda
  C5: TU-152 (C5=T → Válido) vs TU-155 (C5=F → Erro)             — apenas C5 muda
  C6: TU-152 (C6=T → Válido) vs TU-156 (C6=F → Erro)             — apenas C6 muda
  C2: TU-152 (C2=F → Válido) vs TU-157 (C2=T, C3=F → Erro)       — C2 muda, C3=F em ambos
  C3: TU-157 (C3=F → Erro)   vs TU-158 (C3=T → Válido)           — apenas C3 muda
"""

import pytest

from api.services.plan_service import PlanValidationError, validate_plan


@pytest.mark.parametrize(
    "test_id, payload, esperado",
    [
        # TU-152: base válida — C1=T, C2=F, C4=T, C5=T, C6=T → Válido
        ("TU-152",
         {"type": "regular", "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "ok"),

        # TU-153: tipo inválido — C1=F → Erro  (par de C1 com TU-152)
        ("TU-153",
         {"type": "invalido", "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "erro"),

        # TU-154: temperatura fora do intervalo — C4=F → Erro  (par de C4 com TU-152)
        ("TU-154",
         {"type": "regular", "temp_min": 17, "humidity_min": 60, "luminosity_min": 15000},
         "erro"),

        # TU-155: humidade fora do intervalo — C5=F → Erro  (par de C5 com TU-152)
        ("TU-155",
         {"type": "regular", "temp_min": 23, "humidity_min": 35, "luminosity_min": 15000},
         "erro"),

        # TU-156: luminosidade fora do intervalo — C6=F → Erro  (par de C6 com TU-152)
        ("TU-156",
         {"type": "regular", "temp_min": 23, "humidity_min": 60, "luminosity_min": 4000},
         "erro"),

        # TU-157: pontual sem authorização — C2=T, C3=F → Erro  (par de C2 com TU-152)
        ("TU-157",
         {"type": "pontual", "authorized_by": None,
          "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "erro"),

        # TU-158: pontual com autorização — C2=T, C3=T → Válido  (par de C3 com TU-157)
        ("TU-158",
         {"type": "pontual", "authorized_by": "responsavel",
          "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "ok"),
    ],
)
def test_validate_plan_whitebox(test_id, payload, esperado):
    """MC/DC: validate_plan — subconjunto mínimo de 7 casos que provam independência de C1-C6 (TU-152 a TU-158)."""
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)
