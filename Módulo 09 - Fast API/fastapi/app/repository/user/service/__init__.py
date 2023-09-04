from app.repository.user.custom_exceptions import UserNotFoundError, InvalidPasswordError, InternalServerError
from app.repository.user.models.user_models import UserIn, UserOut, UserId, UserForm
from app.repository.user.models.repository_interface import IUserRepository
from app.repository.user.models.service_interface import IUserService
from app.repository.user.service.hashing import Hasher
from app.sqlalchemy.schema import UserSchema
from app.sqlalchemy import Session
from sqlalchemy.orm import Session as SQLAlchemySession
from sqlalchemy.exc import SQLAlchemyError
import uuid


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self._repository = repository

    def get_user_by_id_service(self, user_id: str) -> UserOut:

        client: SQLAlchemySession = Session()

        try:
            user = self._repository.get_user_by_id_repository(client, user_id)

            if not user:
                raise UserNotFoundError(id=user_id)
            
            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email
            )

        except SQLAlchemyError as error:
            client.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error
        finally:
            client.close()


    def get_users_service(self) -> list[UserOut] | list:

        client: SQLAlchemySession = Session()

        try:
            users = self._repository.get_users_repository(client)

            if not users:
                return []
            
            return [UserOut(id=user.id, name=user.name, email=user.email) for user in users]

        except SQLAlchemyError as error:
            client.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error
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

            return UserId(id=new_user.id)

        except SQLAlchemyError as error:
            client.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error
        finally:
            client.close()


    def check_user_service(self, form: UserForm) -> UserOut:

        client: SQLAlchemySession = Session()

        try:
            user = self._repository.get_user_by_name_repository(client, form.name)

            if not user:
                raise UserNotFoundError(name=form.name)

            if Hasher.verify_password(form.password, user.password):
                return UserOut(
                    id=user.id,
                    name=user.name,
                    email=user.email
                )
            else:
                raise InvalidPasswordError(name=form.name)

        except SQLAlchemyError as error:
            client.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error
        finally:
            client.close()  


    def update_user_service(self, user_id: str, user_updated: UserIn) -> UserOut:

        client: SQLAlchemySession = Session()

        try:
            user = self._repository.get_user_by_id_repository(client, user_id)

            if not user:
                raise UserNotFoundError(id=user_id)

            user.name = user_updated.name
            user.email = user_updated.email
            user.password = Hasher.get_password_hash(user_updated.password)

            self._repository.update_user_repository(client, user)

            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email
            )

        except SQLAlchemyError as error:
            client.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error
        finally:
            client.close()


    def delete_user_service(self, user_id: str) -> None:

        client: SQLAlchemySession = Session()

        try:
            user = self._repository.get_user_by_id_repository(client, user_id)

            if not user:
                raise UserNotFoundError(id=user_id)

            self._repository.delete_user_repository(client, user)

        except SQLAlchemyError as error:
            client.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error
        finally:
            client.close()