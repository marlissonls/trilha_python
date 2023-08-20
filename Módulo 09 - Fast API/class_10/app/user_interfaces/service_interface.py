from app.user_interfaces.user_models import UserIn, UserOut, UserId
from abc import ABC, abstractmethod


class IUserService(ABC):

    @abstractmethod
    def get_user_by_id_service(self, user_id: str) -> UserOut:
        pass

    @abstractmethod
    def get_user_by_index_service(self, index: int) -> UserOut:
        pass

    @abstractmethod
    def get_users_service(self) -> list[UserOut]:
        pass

    @abstractmethod
    def create_user_service(self, user: UserIn) -> UserId:
        pass

    @abstractmethod
    def update_user_service(self, user_id: str, user_updated: UserIn) -> UserOut:
        pass

    @abstractmethod
    def delete_user_service(self, user_id: str) -> None:
        pass