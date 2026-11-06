import json
import os

from tests.credentials import TEST_USERS


os.environ.setdefault(
    "GREENHERB_JWT_SECRET",
    os.urandom(32).hex(),
)
os.environ.setdefault(
    "GREENHERB_USERS_JSON",
    json.dumps(
        [{"username": username, **user} for username, user in TEST_USERS.items()]
    ),
)
