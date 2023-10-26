from app.helpers import hash_decoder, hash_encoder
from app.base_models import UserIn, UserOut, UserId
from app.database import DATABASE_PATH
from typing import Any
import json
import uuid

class UserRepository:

    _database = f"{DATABASE_PATH}/db.json"

    def create_user_repository(self, user: UserIn) -> UserId:
        
        user_dict = hash_encoder(user)

        with open(self._database, "r") as db_json:
            users: list[dict[str, Any]] = json.load(db_json)

        user_dict['id'] = str(uuid.uuid1())

        users.append(user_dict)

        with open(self._database, "w") as db_json:
            json.dump(users, db_json)

        return UserId(**{'id': user_dict['id']})


    def get_user_by_id_repository(self, user_id: str) -> UserOut | None:

        with open(self._database, "r") as db_json:
            users: list[dict[str, Any]] = json.load(db_json)
        
        for user in users:
            if user['id'] == user_id:

                return UserOut(**user)

        return None


    def get_users_repository(self) -> list[UserOut] | None:

        with open(self._database, "r") as db_json:
            users: list[dict[str, Any]] = json.load(db_json)
        
        if len(users) == 0:
            return None
        
        users_response = [UserOut(**user) for user in users]

        return users_response
    

    def get_user_by_index_repository(self, index: str) -> UserOut | None:

        with open(self._database, "r") as db_json:
            users: list[dict[str, Any]] = json.load(db_json)

        if len(users) - 1 >= int(index):

                return UserOut(**users[int(index)])

        return None
    

    def update_user_repository(self, user_id: str, user_updated: UserIn) -> UserOut | None:

        with open(self._database, "r") as db_json:
            users: list[dict[str, Any]] = json.load(db_json)
        
        index = None
        for user in users:
            if str(user['id']) == user_id:
                index = users.index(user)
                break

        if index is not None:
            users[index]['name'] = user_updated.name
            users[index]['email'] = user_updated.email
            users[index]['password'] = user_updated.password
        
            with open(self._database, "w") as db_json:
                json.dump(users, db_json)
            
            return UserOut(**users[index])
        else:
            return index


    def delete_user_repository(self, user_id) -> int | None:

        with open(self._database, "r") as db_json:
            users: list[dict[str, Any]] = json.load(db_json)
        
        index = None
        for user in users:
            if str(user['id']) == user_id:
                index = users.index(user)
                break
        
        if index is not None:
            remaining_users = [user for user in users if str(user['id']) != user_id]

            with open(self._database, "w") as db_json:
                    json.dump(remaining_users, db_json)
            
            return index
        else:
            return index