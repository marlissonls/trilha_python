from app.repository.user.models.repository_interface import IUserRepository
from app.repository.user.models.user_models import UserIn
from app.sqlalchemy.schema import UserSchema
from sqlalchemy.orm import Session as SQLAlchemySession
from fastapi import HTTPException, status
from typing import Any, List
import json


class UserRepository(IUserRepository):

    def get_user_by_id_repository(self, client: SQLAlchemySession, user_id) -> UserSchema | None:

        user = client.query(UserSchema).filter(UserSchema.id == user_id).first()

        return user


    def get_users_repository(self, client:SQLAlchemySession) -> List[UserSchema]:

        users = client.query(UserSchema).all()

        return users


    def create_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:

        client.add(user)
        client.commit()


    def update_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:

        client.merge(user)
        client.commit()


    def delete_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:

        client.delete(user)
        client.commit()