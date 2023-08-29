from app.repository.user.models.user_models import UserIn, UserOut, UserId
from abc import ABC, abstractmethod


class IUserController(ABC):

    @abstractmethod
    def get_user_by_id_controller(self, user_id: str) -> UserOut:
        pass

    @abstractmethod
    def get_user_by_index_controller(self, index: str) -> UserOut:
        pass

    @abstractmethod
    def get_users_controller(self) -> list[UserOut]:
        pass

    @abstractmethod
    def create_user_controller(self, user: UserIn) -> UserId:
        pass

    @abstractmethod
    def update_user_controller(self, user_id: str, user: UserIn) -> UserOut:
        pass

    @abstractmethod
    def delete_user_controller(self, user_id: str) -> None:
        pass