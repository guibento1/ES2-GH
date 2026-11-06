import pytest

from api.services.plan_service import PlanValidationError, validate_plan


@pytest.mark.parametrize(
    "test_id, payload, esperado",
    [
        # TU-158: base válida — C1=T, C2=F, C4=T, C5=T, C6=T → Válido
        ("TU-158",
         {"type": "regular", "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "ok"),

        # TU-159: tipo inválido — C1=F → Erro  (par de C1 com TU-158)
        ("TU-159",
         {"type": "invalido", "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "erro"),

        # TU-160: temperatura fora do intervalo — C4=F → Erro  (par de C4 com TU-158)
        ("TU-160",
         {"type": "regular", "temp_min": 17, "humidity_min": 60, "luminosity_min": 15000},
         "erro"),

        # TU-161: humidade fora do intervalo — C5=F → Erro  (par de C5 com TU-158)
        ("TU-161",
         {"type": "regular", "temp_min": 23, "humidity_min": 35, "luminosity_min": 15000},
         "erro"),

        # TU-162: luminosidade fora do intervalo — C6=F → Erro  (par de C6 com TU-158)
        ("TU-162",
         {"type": "regular", "temp_min": 23, "humidity_min": 60, "luminosity_min": 4000},
         "erro"),

        # TU-163: pontual sem authorização — C2=T, C3=F → Erro  (par de C2 com TU-158)
        ("TU-163",
         {"type": "pontual", "authorized_by": None,
          "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "erro"),

        # TU-164: pontual com autorização — C2=T, C3=T → Válido  (par de C3 com TU-163)
        ("TU-164",
         {"type": "pontual", "authorized_by": "responsavel",
          "temp_min": 23, "humidity_min": 60, "luminosity_min": 15000},
         "ok"),
    ],
)
def test_validate_plan_whitebox(test_id, payload, esperado):
    """MC/DC: validate_plan — subconjunto mínimo de 7 casos que provam independência de C1-C6 (TU-158 a TU-164)."""
    if esperado == "erro":
        with pytest.raises(PlanValidationError):
            validate_plan(payload)
    else:
        validate_plan(payload)


# ---------------------------------------------------------------------------
# TU-165 a TU-169 — White-box adicional: cobertura de ramos fora da decisão MC/DC
# Atinge as linhas defensivas e regras max/min que não fazem parte da expressão
# composta principal mas são branches do código real de validate_plan.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, payload, esperado",
    [
        # TU-165: payload não é dict → cobre o guard clause inicial
        ("TU-165", None, "erro"),

        # TU-166: temp_min com tipo errado (string) → cobre _check_numeric_range type-check
        ("TU-166",
         {"type": "regular", "temp_min": "muito"},
         "erro"),

        # TU-167: temp_max < temp_min → cobre o branch de consistência max/min
        ("TU-167",
         {"type": "regular", "temp_min": 26, "temp_max": 22},
         "erro"),

        # TU-168: humidity_max < humidity_min → cobre o branch de consistência max/min
        ("TU-168",
         {"type": "regular", "humidity_min": 70, "humidity_max": 50},
         "erro"),

        # TU-169: luminosity_max < luminosity_min → cobre o branch de consistência max/min
        ("TU-169",
         {"type": "regular", "luminosity_min": 20000, "luminosity_max": 10000},
         "erro"),
    ],
)
def test_validate_plan_whitebox_branches_adicionais(test_id, payload, esperado):
    """White-box: ramos fora da decisão MC/DC principal (TU-165 a TU-169)."""
    with pytest.raises(PlanValidationError):
        validate_plan(payload)
