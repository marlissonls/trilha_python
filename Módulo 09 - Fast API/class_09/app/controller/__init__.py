from app.service import UserService
from app.base_models import UserIn, UserOut, UserId


class UserController:

    def __init__(self):
        self.service = UserService()


    def create_user_controller(self, user: UserIn) -> UserId:

        result = self.service.create_user_service(user)

        return result


    def get_user_by_id_controller(self, user_id: str) -> UserOut:

        result = self.service.get_user_by_id_service(user_id)

        return result


    def get_users_controller(self) -> list[UserOut]:

        result = self.service.get_users_service()

        return result
    

    def get_user_by_index_controller(self, index: str) -> UserOut:

        result = self.service.get_user_by_index_service(index)

        return result
    

    def update_user_controller(self, user_id: str, user: UserIn) -> UserOut:

        result = self.service.update_user_service(user_id, user)

        return result
    

    def delete_user_controller(self, user_id: str) -> None:

        self.service.delete_user_service(user_id)