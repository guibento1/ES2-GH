"""In-memory data store for the GREENHERB API."""

from copy import deepcopy


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

USERS = [
    {"id": 1, "username": "tecnico",     "password": "tecnico123",     "full_name": "Técnico de Estufa",       "role": "Técnico"},
    {"id": 2, "username": "responsavel", "password": "responsavel123", "full_name": "Responsável Técnico",     "role": "Responsável Técnico"},
    {"id": 3, "username": "admin",       "password": "admin123",       "full_name": "Administrador GREENHERB", "role": "Administrador"},
]

REFRESH_TOKENS = {}

_next_user_id = len(USERS) + 1


def add_user(data):
    global _next_user_id
    user = {"id": _next_user_id, **data}
    _next_user_id += 1
    USERS.append(user)
    return deepcopy(user)


def find_user_by_username(username):
    for user in USERS:
        if user["username"] == username:
            return deepcopy(user)
    return None


def public_user(user):
    if user is None:
        return None
    u = deepcopy(user)
    u.pop("password", None)
    return u


# ---------------------------------------------------------------------------
# Herbs — seeded from the aromatic herb catalogue
# ---------------------------------------------------------------------------

HERBS = [
    {"id": 1, "name": "Manjericão",    "family": "Lamiaceae", "description": "Erva aromática muito usada na culinária mediterrânica."},
    {"id": 2, "name": "Tomilho",       "family": "Lamiaceae", "description": "Aroma intenso e terroso; utilizado em infusões e cozinhados."},
    {"id": 3, "name": "Orégão",        "family": "Lamiaceae", "description": "Indispensável na culinária italiana e nas pizzas."},
    {"id": 4, "name": "Menta",         "family": "Lamiaceae", "description": "Sabor refrescante; usada em chás, cocktails e culinária."},
    {"id": 5, "name": "Rosmaninho",    "family": "Lamiaceae", "description": "Erva resistente com propriedades antioxidantes e medicinais."},
    {"id": 6, "name": "Salva",         "family": "Lamiaceae", "description": "Folhas prateadas com aroma suave; popular no sul da Europa."},
    {"id": 7, "name": "Coentros",      "family": "Apiaceae",  "description": "Sabor cítrico e intenso; base da gastronomia portuguesa."},
    {"id": 8, "name": "Erva-cidreira", "family": "Lamiaceae", "description": "Aroma a limão; usada em chás calmantes e digestivos."},
]

_next_herb_id = len(HERBS) + 1


def list_herbs():
    return deepcopy(HERBS)


def add_herb(data):
    global _next_herb_id
    herb = {"id": _next_herb_id, **data}
    _next_herb_id += 1
    HERBS.append(herb)
    return deepcopy(herb)


def reset_herbs(seed=None):
    global _next_herb_id
    HERBS.clear()
    if seed:
        HERBS.extend(deepcopy(seed))
    _next_herb_id = len(HERBS) + 1


# ---------------------------------------------------------------------------
# Plans
# ---------------------------------------------------------------------------

PLANS = []

_next_plan_id = 1


def list_plans():
    return deepcopy(PLANS)


def add_plan(data):
    global _next_plan_id
    plan = {"id": _next_plan_id, **data}
    _next_plan_id += 1
    PLANS.append(plan)
    return deepcopy(plan)


def find_plan_by_id(plan_id):
    for p in PLANS:
        if p["id"] == plan_id:
            return deepcopy(p)
    return None


def reset_plans():
    global _next_plan_id
    PLANS.clear()
    _next_plan_id = 1


# ---------------------------------------------------------------------------
# Batches
# ---------------------------------------------------------------------------

BATCHES = [
    {
        "id": 1, "herb_id": 1, "plan_id": None,
        "state": "ativo", "planned_qty": 100.0,
        "actual_qty": None, "losses": None, "productivity": None,
    },
]

_next_batch_id = len(BATCHES) + 1


def list_batches():
    return deepcopy(BATCHES)


def add_batch(data):
    global _next_batch_id
    batch = {"id": _next_batch_id, **data}
    _next_batch_id += 1
    BATCHES.append(batch)
    return deepcopy(batch)


def find_batch_by_id(batch_id):
    for b in BATCHES:
        if b["id"] == batch_id:
            return deepcopy(b)
    return None


def update_batch(batch_id, updates):
    for b in BATCHES:
        if b["id"] == batch_id:
            b.update(updates)
            return deepcopy(b)
    return None


def reset_batches(seed=None):
    global _next_batch_id
    BATCHES.clear()
    if seed:
        BATCHES.extend(deepcopy(seed))
    _next_batch_id = len(BATCHES) + 1


# ---------------------------------------------------------------------------
# Alerts
# ---------------------------------------------------------------------------

ALERTS = []

_next_alert_id = 1


def list_alerts():
    return deepcopy(ALERTS)


def add_alert(data):
    global _next_alert_id
    alert = {"id": _next_alert_id, "state": "pendente", **data}
    _next_alert_id += 1
    ALERTS.append(alert)
    return deepcopy(alert)


def find_alert_by_id(alert_id):
    for a in ALERTS:
        if a["id"] == alert_id:
            return deepcopy(a)
    return None


def update_alert(alert_id, updates):
    for a in ALERTS:
        if a["id"] == alert_id:
            a.update(updates)
            return deepcopy(a)
    return None


def reset_alerts():
    global _next_alert_id
    ALERTS.clear()
    _next_alert_id = 1


# ---------------------------------------------------------------------------
# Measurements
# ---------------------------------------------------------------------------

MEASUREMENTS = []

_next_measurement_id = 1


def list_measurements():
    return deepcopy(MEASUREMENTS)


def add_measurement(data):
    global _next_measurement_id
    m = {"id": _next_measurement_id, **data}
    _next_measurement_id += 1
    MEASUREMENTS.append(m)
    return deepcopy(m)


def reset_measurements():
    global _next_measurement_id
    MEASUREMENTS.clear()
    _next_measurement_id = 1
