from app.repository.user.models.user_models import UserIn, UserOut, UserId
from app.repository.user.models.repository_interface import IUserRepository
from app.repository.user.models.service_interface import IUserService
from app.repository.user.service.hashing import Hasher
from app.sqlalchemy.schema import UserSchema
from app.sqlalchemy import Session
from sqlalchemy.orm import Session as SQLAlchemySession
from fastapi import HTTPException, status
import uuid


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self._repository = repository
        self._internal_server_error_500 = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error.")


    def get_user_by_id_service(self, user_id: str) -> UserOut:

        client: SQLAlchemySession = Session()

        try:
            user = self._repository.get_user_by_id_repository(client, user_id)

            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            return UserOut(*user)
        finally:
            client.close()


    def get_user_by_index_service(self, index: int) -> UserOut:

        users_list = self._repository.get_users_repository()

        if len(users_list) - 1 >= index:

            return UserOut(**users_list[index])

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user on index {index}.")


    def get_users_service(self) -> list[UserOut] | list:

        client: SQLAlchemySession = Session()

        try:
            users = self._repository.get_users_repository(client)

            if not users:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find users.")
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            return UserOut(**users)
        finally:
            client.close()


    def create_user_service(self, user: UserIn) -> UserId:

        client: SQLAlchemySession = Session()

        try:
            new_user = UserSchema(
                id=str(uuid.uuid1()),
                name=user.name,
                email=user.email,
                password=Hasher.get_password_hash(user.password)
            )

            self._repository.create_user_repository(client, new_user)
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            return UserId(**{'id': new_user.id})
        finally:
            client.close()


    def update_user_service(self, user_id: str, user_updated: UserIn) -> UserOut:

        client: SQLAlchemySession = Session()

        try:
            user = self._repository.get_user_by_id_repository(client, user_id)

            if user is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            user.name = user_updated.name
            user.email = user_updated.email
            user.password = user_updated.password

            self._repository.update_user_repository(user)

            return UserOut(**user)
        finally:
            client.close()


    def delete_user_service(self, user_id: str) -> None:

        client: SQLAlchemySession = Session()

        try:
            user = self._repository.get_user_by_id_repository(client, user_id)

            if user is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            self._repository.delete_user_repository(user)
        finally:
            client.close()