from app.repository.user.models.service_interface import IUserService
from app.repository.user.models.controller_interface import IUserController
from app.repository.user.models.user_models import UserIn, UserOut, UserId, UserForm
from fastapi import HTTPException
import logging


logger = logging.getLogger(__name__)


class UserControllerException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class UserController(IUserController):

    def __init__(self, service: IUserService):
        self._service = service

    def get_user_by_id_controller(self, user_id: str) -> UserOut:

        try:
            result = self._service.get_user_by_id_service(user_id)
            return result
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch user by ID.") from error


    def get_users_controller(self) -> list[UserOut] | list:

        try:
            result = self._service.get_users_service()
            return result
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch users.") from error


    def create_user_controller(self, user: UserIn) -> UserId:
        try:
            result = self._service.create_user_service(user)
            return result
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to create user.") from error


    def check_user_controller(self, form: UserForm) -> UserOut:
        try:
            result = self._service.check_user_service(form)
            return result
        except HTTPException as http_error:
            logger.error("An error occurred: %s", http_error)
            raise HTTPException from http_error
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch user by name.") from error


    def update_user_controller(self, user_id: str, user: UserIn) -> UserOut:

        try:
            result = self._service.update_user_service(user_id, user)
            return result
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to update user.") from error


    def delete_user_controller(self, user_id: str) -> None:

        try:
            self._service.delete_user_service(user_id)
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to delete user.") from error