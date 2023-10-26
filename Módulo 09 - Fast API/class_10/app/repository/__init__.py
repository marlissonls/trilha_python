from fastapi import HTTPException, status
from app.user_interfaces.repository_interface import IUserRepository
from typing import Any
import json


class UserRepository(IUserRepository):

    def __init__(self, database: str) -> None:
        self._database = database
        self._internal_server_error_500 = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")


    def get_users_repository(self) -> list[dict[str, Any]]:

        try: 
            with open(self._database, "r") as db_json:
                users_list: list[dict[str, Any]] = json.load(db_json)
        except:
            raise self._internal_server_error_500
        else:
            return users_list


    def create_user_repository(self, users_list: list[dict[str, Any]]) -> None:

        try:
            with open(self._database, "w") as db_json:
                json.dump(users_list, db_json)
        except:
            raise self._internal_server_error_500


    def update_user_repository(self, users_list: list[dict[str, Any]]) -> None:

        try:
            with open(self._database, "w") as db_json:
                json.dump(users_list, db_json)
        except:
            raise self._internal_server_error_500


    def delete_user_repository(self, users_list: list[dict[str, Any]]) -> None:

        try:
            with open(self._database, "w") as db_json:
                json.dump(users_list, db_json)
        except:
            raise self._internal_server_error_500