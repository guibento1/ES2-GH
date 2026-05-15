"""
Testes de unidade — Sprint 3
Módulo: api.services.alert_service  (TU-57 a TU-64)

Técnica: Cobertura de Condições Múltiplas + MC/DC

Decisão composta: resultado = (C1 OR C2) AND C3
  C1: temp    > limits['temp_max']
  C2: humidity < limits['humidity_min']
  C3: sensor_ok

Tabela de verdade completa (2^3 = 8 combinações):

  #   C1  C2  C3  (C1∨C2)∧C3  Resultado
  1   F   F   F       F        None
  2   F   F   T       F        None
  3   F   T   F       F        None
  4   F   T   T       T        "Aviso"
  5   T   F   F       F        None
  6   T   F   T       T        "Aviso"
  7   T   T   F       F        None
  8   T   T   T       T        "Crítico"

Subconjunto MC/DC (mínimo que demonstra independência de cada condição):
  C1 independente: linhas 2 vs 6  (C1: F→T, C2=F, C3=T → None→Aviso)
  C2 independente: linhas 2 vs 4  (C2: F→T, C1=F, C3=T → None→Aviso)
  C3 independente: linhas 4 vs 3  (C3: T→F, C1=F, C2=T → Aviso→None)
"""

import pytest

from api.services.alert_service import classify_alert


# Limites de referência usados em todos os testes
LIMITS = {"temp_max": 28.0, "humidity_min": 40.0}


@pytest.mark.parametrize(
    "test_id, temp,  hum,  sensor_ok, esperado",
    [
        # ---- Tabela de verdade completa (TU-57 a TU-64) ----
        # C1=F, C2=F, C3=F  →  (F∨F)∧F = F  →  None
        ("TU-57", 23.0, 60.0, False, None),

        # C1=F, C2=F, C3=T  →  (F∨F)∧T = F  →  None
        ("TU-58", 23.0, 60.0, True,  None),

        # C1=F, C2=T, C3=F  →  (F∨T)∧F = F  →  None
        ("TU-59", 23.0, 35.0, False, None),

        # C1=F, C2=T, C3=T  →  (F∨T)∧T = T  →  "Aviso"   ★ MC/DC par C2
        ("TU-60", 23.0, 35.0, True,  "Aviso"),

        # C1=T, C2=F, C3=F  →  (T∨F)∧F = F  →  None
        ("TU-61", 30.0, 60.0, False, None),

        # C1=T, C2=F, C3=T  →  (T∨F)∧T = T  →  "Aviso"   ★ MC/DC par C1
        ("TU-62", 30.0, 60.0, True,  "Aviso"),

        # C1=T, C2=T, C3=F  →  (T∨T)∧F = F  →  None      ★ MC/DC par C3
        ("TU-63", 30.0, 35.0, False, None),

        # C1=T, C2=T, C3=T  →  (T∨T)∧T = T  →  "Crítico"
        ("TU-64", 30.0, 35.0, True,  "Crítico"),
    ],
)
def test_classify_alert(test_id, temp, hum, sensor_ok, esperado):
    """
    Cobertura de Condições Múltiplas + MC/DC sobre classify_alert (TU-57 a TU-64).
    Exercita todas as 8 combinações de (C1, C2, C3).
    """
    result = classify_alert(temp, hum, LIMITS, sensor_ok)
    assert result == esperado, (
        f"[{test_id}] C1={temp > LIMITS['temp_max']}, "
        f"C2={hum < LIMITS['humidity_min']}, C3={sensor_ok} "
        f"→ esperado '{esperado}', obtido '{result}'"
    )
