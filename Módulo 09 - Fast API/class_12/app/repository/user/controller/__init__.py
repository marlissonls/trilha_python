from app.repository.user.models.service_interface import IUserService
from app.repository.user.models.controller_interface import IUserController
from app.repository.user.models.user_models import UserIn, UserOut, UserId
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