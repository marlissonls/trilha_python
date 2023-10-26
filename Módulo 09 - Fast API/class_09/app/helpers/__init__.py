from app.base_models import UserIn
from app.configs import configs
from typing import Any

def hash_encoder(user: UserIn) -> dict[str, Any]:

    user_dict = user.model_dump()

    user_dict['password'] = configs['secret'] + user_dict['password']
    
    return user_dict


def hash_decoder(user: dict[str, Any]) -> UserIn:

    user['password'] = user['password'][5:]

    user_model = UserIn(**user)

    return user_model