from app.user_interfaces.user_models import UserIn, UserOut, UserId
from app.user_interfaces.repository_interface import IUserRepository
from app.user_interfaces.service_interface import IUserService
from app.service.hashing import Hasher
from fastapi import HTTPException, status
import uuid


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self._repository = repository


    def get_user_by_id_service(self, user_id: str) -> UserOut:

        users_list = self._repository.get_users_repository()

        for user in users_list:
            if user['id'] == user_id:
                return UserOut(**user)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")


    def get_user_by_index_service(self, index: int) -> UserOut:

        users_list = self._repository.get_users_repository()

        if len(users_list) - 1 >= index:

            return UserOut(**users_list[index])

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user on index {index}.")


    def get_users_service(self) -> list[UserOut] | list:

        users_list = self._repository.get_users_repository()

        if len(users_list) > 0:
            return [UserOut(**user) for user in users_list]
        else:
            return []


    def create_user_service(self, user: UserIn) -> UserId:

        new_user = user.model_dump()
        new_user['password'] = Hasher.get_password_hash(new_user['password'])
        new_user['id'] = str(uuid.uuid1())

        users_list = self._repository.get_users_repository()

        users_list.append(new_user)

        self._repository.create_user_repository(users_list)

        return UserId(**{'id': new_user['id']})


    def update_user_service(self, user_id: str, user_updated: UserIn) -> UserOut:

        users_list = self._repository.get_users_repository()

        index = None
        for user in users_list:
            if str(user['id']) == user_id:
                index = users_list.index(user)
                break

        if index is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")

        else:
            users_list[index]['name'] = user_updated.name
            users_list[index]['email'] = user_updated.email
            users_list[index]['password'] = user_updated.password

            self._repository.update_user_repository(users_list)

            return UserOut(**users_list[index])


    def delete_user_service(self, user_id: str) -> None:

        users_list = self._repository.get_users_repository()

        index = None
        for user in users_list:
            if str(user['id']) == user_id:
                index = users_list.index(user)
                break
        
        if index is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")

        else:
            remaining_users = [user for user in users_list if user['id'] != user_id]

            self._repository.delete_user_repository(remaining_users)