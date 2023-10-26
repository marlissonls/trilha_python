from abc import ABC, abstractmethod
from typing import Any


class IUserRepository(ABC):

    @abstractmethod
    def get_users_repository(self) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def create_user_repository(self, users_list: list[dict[str, Any]]) -> None:
        pass

    @abstractmethod
    def update_user_repository(self, users_list: list[dict[str, Any]]) -> None:
        pass

    @abstractmethod
    def delete_user_repository(self, users_list: list[dict[str, Any]]) -> None:
        pass