from app.sqlalchemy.schema import UserSchema
from app.repository.user.models.user_models import UserIn
from sqlalchemy.orm import Session as SQLAlchemySession
from abc import ABC, abstractmethod
from typing import Any, List


class IUserRepository(ABC):

    @abstractmethod
    def get_user_by_id_repository(self, client: SQLAlchemySession, user_id: str) -> UserSchema | None:
        pass

    @abstractmethod
    def get_users_repository(self, client: SQLAlchemySession) -> List[UserSchema]:
        pass
    
    @abstractmethod
    def get_user_by_name_repository(self, client: SQLAlchemySession, name: str) -> UserSchema | None:
        pass

    @abstractmethod
    def create_user_repository(self, client: SQLAlchemySession, user: UserIn) -> None:
        pass

    @abstractmethod
    def update_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:
        pass

    @abstractmethod
    def delete_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:
        pass