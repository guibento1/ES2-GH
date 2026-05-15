"""In-memory data store for the GREENHERB API."""

from copy import deepcopy


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

USERS = [
    {
        "id": 1,
        "username": "tecnico",
        "password": "tecnico123",
        "full_name": "Técnico de Estufa",
        "role": "Técnico",
    },
    {
        "id": 2,
        "username": "responsavel",
        "password": "responsavel123",
        "full_name": "Responsável Técnico",
        "role": "Responsável Técnico",
    },
    {
        "id": 3,
        "username": "admin",
        "password": "admin123",
        "full_name": "Administrador GREENHERB",
        "role": "Administrador",
    },
]

REFRESH_TOKENS = {}


def find_user_by_username(username):
    """Return a copy of the user matching the supplied username."""
    for user in USERS:
        if user["username"] == username:
            return deepcopy(user)
    return None


def public_user(user):
    """Return user data without the password field."""
    if user is None:
        return None
    user_data = deepcopy(user)
    user_data.pop("password", None)
    return user_data


# ---------------------------------------------------------------------------
# Herbs — seeded from the aromatic herb catalogue
# ---------------------------------------------------------------------------

HERBS = [
    {"id": 1, "name": "Manjericão",    "family": "Lamiaceae", "description": "Erva aromática muito usada na culinária mediterrânica."},
    {"id": 2, "name": "Tomilho",       "family": "Lamiaceae", "description": "Aroma intenso e terroso; utilizado em infusões e cozinhados."},
    {"id": 3, "name": "Orégão",        "family": "Lamiaceae", "description": "Indispensável na culinária italiana e nas pizzas."},
    {"id": 4, "name": "Menta",         "family": "Lamiaceae", "description": "Sabor refrescante; usada em chás, cocktails e culinária."},
    {"id": 5, "name": "Rosmaninho",    "family": "Lamiaceae", "description": "Erva resistente com propriedades antioxidantes e medicinais."},
    {"id": 6, "name": "Salva",         "family": "Lamiaceae", "description": "Folhas prateadas com aroma suave; popular em receitas do sul da Europa."},
    {"id": 7, "name": "Coentros",      "family": "Apiaceae",  "description": "Sabor cítrico e intenso; base da gastronomia portuguesa e asiática."},
    {"id": 8, "name": "Erva-cidreira", "family": "Lamiaceae", "description": "Aroma a limão; usada em chás calmantes e digestivos."},
]

_next_herb_id = len(HERBS) + 1


def list_herbs():
    """Return a deep copy of all herbs."""
    return deepcopy(HERBS)


def add_herb(data):
    """Persist a new herb and return it with its assigned id."""
    global _next_herb_id
    herb = {"id": _next_herb_id, **data}
    _next_herb_id += 1
    HERBS.append(herb)
    return deepcopy(herb)


def reset_herbs(seed=None):
    """Replace the herbs store — used in tests to guarantee a clean state."""
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
    """Return a deep copy of all plans."""
    return deepcopy(PLANS)


def add_plan(data):
    """Persist a new plan and return it with its assigned id."""
    global _next_plan_id
    plan = {"id": _next_plan_id, **data}
    _next_plan_id += 1
    PLANS.append(plan)
    return deepcopy(plan)


def reset_plans():
    """Replace the plans store — used in tests."""
    global _next_plan_id
    PLANS.clear()
    _next_plan_id = 1
