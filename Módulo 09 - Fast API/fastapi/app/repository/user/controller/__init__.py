from app.repository.user.models.service_interface import IUserService
from app.repository.user.models.controller_interface import IUserController
from app.repository.user.models.user_models import UserIn, UserOut, UserId, UserForm
from app.repository.user.custom_exceptions import UserNotFoundError, InvalidPasswordError, UserControllerException
from typing import Annotated
from fastapi import UploadFile
import logging


logger = logging.getLogger(__name__)


class UserController(IUserController):

    def __init__(self, service: IUserService):
        self._service = service

    def get_user_by_id_controller(self, user_id: str) -> UserOut:
        try:
            return self._service.get_user_by_id_service(user_id)
        except UserNotFoundError as error:
            logger.error("User not found: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch user by ID.") from error


    def get_users_controller(self) -> list[UserOut] | list:
        try:
            return self._service.get_users_service()
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch users.") from error


    def create_user_controller(
        self, 
        name: str,
        email: str,
        password: str,
        profile_image: UploadFile
    ) -> UserId:
        try:
            return self._service.create_user_service(
                name,
                email,
                password,
                profile_image
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to create user.") from error


    def check_user_controller(self, form: UserForm) -> UserOut:
        try:
            return self._service.check_user_service(form)
        except UserNotFoundError as error:
            logger.error("User not found: %s", error)
            raise
        except InvalidPasswordError as error:
            logger.error("Invalid password: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch user by name.") from error


    def update_user_controller(self, user_id: str, user: UserIn) -> UserOut:
        try:
            return self._service.update_user_service(user_id, user)
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to update user.") from error


    def delete_user_controller(self, user_id: str) -> None:
        try:
            self._service.delete_user_service(user_id)
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to delete user.") from error
