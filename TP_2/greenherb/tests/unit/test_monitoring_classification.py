import pytest

from api.services.monitoring_service import classify_temperature


# ---------------------------------------------------------------------------
# TU-180 a TU-186 — Particionamento de Equivalência da classificação de
# temperatura (monitoring_service.classify_temperature).
#
# Limites: intervalo normal [18, 28] °C; CRITICAL_DEVIATION = 7 °C.
# Classes de equivalência:
#   Normal          [18, 28]          → None
#   Calor moderado  (28, 35]          → "Informativo"   (desvio 0..7)
#   Calor crítico   (35, +∞)          → "Crítico"       (desvio > 7)
#   Frio moderado   [11, 18)          → "Informativo"   (desvio 0..7)
#   Frio crítico    (-∞, 11)          → "Crítico"       (desvio > 7)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, temp, esperado",
    [
        ("TU-180", 15,  "Informativo"),  # PE: frio moderado [11,18) — representante 15 °C
        ("TU-181", 38,  "Crítico"),      # PE: calor crítico (35,+∞) — representante realista 38 °C
        ("TU-182", 50,  "Crítico"),      # PE: calor crítico (35,+∞) — valor extremo 50 °C
        ("TU-183", 8,   "Crítico"),      # PE: frio crítico (-∞,11) — representante 8 °C
        ("TU-184", -10, "Crítico"),      # PE: frio crítico (-∞,11) — valor extremo abaixo de zero
        ("TU-185", 33,  "Informativo"),  # PE: calor moderado (28,35] — representante 33 °C
        ("TU-186", 20,  None),           # PE: normal [18,28] — representante interior 20 °C
    ],
)
def test_classify_temperature_pe(test_id, temp, esperado):
    """PE: classify_temperature — uma classe de equivalência por representante (TU-180 a TU-186)."""
    assert classify_temperature(temp) == esperado
