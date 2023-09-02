from app.repository.user.models.user_models import UserIn, UserOut, UserId, UserForm
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

            if user is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email
            )
        finally:
            client.close()


    def get_users_service(self) -> list[UserOut]:

        client: SQLAlchemySession = Session()

        try:
            users = self._repository.get_users_repository(client)

            if not users:
                return []
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            return [UserOut(id=user.id, name=user.name, email=user.email) for user in users]
        finally:
            client.close()


    def create_user_service(self, user_body: UserIn) -> UserId:

        client: SQLAlchemySession = Session()

        try:
            new_user = UserSchema(
                id=str(uuid.uuid1()),
                name=user_body.name,
                email=user_body.email,
                password=Hasher.get_password_hash(user_body.password)
            )

            self._repository.create_user_repository(client, new_user)
        except Exception as e:
            raise self._internal_server_error_500 from e
        else:
            return UserId(id=new_user.id)
        finally:
            client.close()
    

    def check_user_service(self, form: UserForm) -> UserOut:

        client: SQLAlchemySession = Session()

        user = self._repository.get_user_by_name_repository(client, form.name)

        if not user:
            client.close()
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by name: {form.name}.")

        if Hasher.verify_password(form.password, user.password):
            client.close()
            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email
            )
        else:
            client.close()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Password do no match.")


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
            user.password = Hasher.get_password_hash(user_updated.password)

            self._repository.update_user_repository(client, user)

            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email
            )
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
            self._repository.delete_user_repository(client, user)
        finally:
            client.close()