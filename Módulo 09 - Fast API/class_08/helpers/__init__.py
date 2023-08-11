from base_models import UserIn

def hash_encoder(users: list):
    for user in users:
        user['password'] = 'HASH_' + user['password']
    return users

def hash_decoder(users: list[UserIn]) -> list[UserIn]:
    for user in users:
        user['password'] = user['password'][5:]
    return users