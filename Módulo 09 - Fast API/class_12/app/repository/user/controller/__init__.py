from app.repository.user.models.service_interface import IUserService
from app.repository.user.models.controller_interface import IUserController
from app.repository.user.models.user_models import UserIn, UserOut, UserId


class UserController(IUserController):

    def __init__(self, service: IUserService):
        self._service = service


    def get_user_by_id_controller(self, user_id: str) -> UserOut:

        try:
            result = self._service.get_user_by_id_service(user_id)
        except Exception as Error:
            print(Error)
        else:
            return result


    def get_users_controller(self) -> list[UserOut] | list:

        try:
            result = self._service.get_users_service()
        except Exception as Error:
            print(Error)
        else:
            return result


    def create_user_controller(self, user: UserIn) -> UserId:

        try:
            result = self._service.create_user_service(user)
        except Exception as Error:
            print(Error)
        else:
            return result


    def update_user_controller(self, user_id: str, user: UserIn) -> UserOut:

        try:
            result = self._service.update_user_service(user_id, user)
        except Exception as Error:
            print(Error)
        else:
            return result


    def delete_user_controller(self, user_id: str) -> None:

        try:
            self._service.delete_user_service(user_id)
        except Exception as Error:
            print(Error)