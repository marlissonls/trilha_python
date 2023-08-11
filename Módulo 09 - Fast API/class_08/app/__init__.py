from fastapi import FastAPI, status
from base_models import UserIn, UserOut
from typing import Any
from helpers import hash_decoder, hash_encoder
from os.path import dirname
import json

""" req body
users = [
    {"name": "hector", "email": "wheel_chair@yahoomail.com.nz", "password": "dingdingding"},
    {"name": "saul", "email": "saul@advmail.com", "password": "kim"},
    {"name": "walterwhite", "email": "babyblue@gmail.com", "password": "heisenberg"},
    {"name": "vince", "email": "yoyoyo@mail.com", "password": "bbad"},
]
"""

api = FastAPI()


@api.post("/users/{users}", status_code=status.HTTP_201_CREATED)
def create_users(users: list[UserIn]) -> Any:

    users_enc = hash_encoder(users)

    with open(f"{dirname(__file__)}/database/db.json", "w") as file_json:
        json.dump(users_enc, file_json)


@api.get("/users/", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users() -> Any:

    with open(f"{dirname(__file__)}/database/db.json", "r") as file_json:
        users_enc = json.load(file_json)

    users_dec = hash_decoder(users_enc)

    return users_dec