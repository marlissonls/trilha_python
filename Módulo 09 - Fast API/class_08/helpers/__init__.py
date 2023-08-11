from base_models import UserIn
from typing import Any


def hash_encoder(users: list[UserIn]) -> list[dict[str, Any]]:

    users_serializable = [user.model_dump() for user in users]

    for user in users_serializable:
        user['password'] = 'HASH_' + user['password']
    
    return users_serializable


def hash_decoder(users: list[dict[str, Any]]) -> list[UserIn]:
    
    for user in users:
        user['password'] = user['password'][5:]

    users_model = [UserIn(**user) for user in users]

    return users_model