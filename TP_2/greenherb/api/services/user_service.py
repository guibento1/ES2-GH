from api.data import memory_store


def list_users():
    return [memory_store.public_user(user) for user in memory_store.USERS]

