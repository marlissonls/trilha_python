from fastapi import FastAPI, status
from base_models import HomePage, UserIn, UserOut
from typing import Any
from helpers import hash_decoder, hash_encoder
from os.path import dirname
import json
from configs import configs

port = configs["port"]

SOURCE = dirname(dirname(__file__))

users_request_body = [
    {"name": "hector", "email": "wheel_chair@yahoomail.com", "password": "HASH_dingdingding"},
    {"name": "suzane", "email": "suzane@gmail.com", "password": "HASH_12345678"},
    {"name": "walterwhite", "email": "babyblue@gmail.com", "password": "HASH_heisenberg"},
    {"name": "vince", "email": "yoyoyo@mail.com", "password": "HASH_bbad"}
]

api = FastAPI()


@api.get("/", status_code=status.HTTP_200_OK, response_model=HomePage)
def home_page() -> Any:

    return {"get_users": f"http://127.0.0.1:{port}/users"}


@api.post("/users/", status_code=status.HTTP_201_CREATED)
def create_users(users: list[UserIn]) -> Any:

    users_enc = hash_encoder(users)

    with open(f"{SOURCE}/database/db.json", "w") as db_json:
        json.dump(users_enc, db_json)


@api.get("/users/", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users() -> Any:

    with open(f"{SOURCE}/database/db.json", "r") as db_json:
        users_enc: list[dict[str, Any]] = json.load(db_json)

    users_dec = hash_decoder(users_enc)

    return users_dec


@api.delete("/users/", status_code=status.HTTP_204_NO_CONTENT)
def delete_users() -> None:

    no_users: list = []

    with open(f"{SOURCE}/database/db.json", "w") as db_json:
        json.dump(no_users, db_json)