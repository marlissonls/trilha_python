from app.repository.user.models.repository_interface import IUserRepository
from app.sqlalchemy.schema import UserSchema
from sqlalchemy.orm import Session as SQLAlchemySession
from typing import List


class UserRepository(IUserRepository):

    def get_user_by_id_repository(self, client: SQLAlchemySession, user_id: str) -> UserSchema | None:

        user = client.query(UserSchema).filter(UserSchema.id == user_id).first()

        return user


    def get_users_repository(self, client: SQLAlchemySession) -> List[UserSchema]:

        users = client.query(UserSchema).all()

        return users
    

    def get_user_by_name_repository(self, client: SQLAlchemySession, name: str) -> UserSchema | None:

        user = client.query(UserSchema).filter(UserSchema.name == name).first()

        return user


    def create_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:

        client.add(user)
        client.commit()


    def update_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:

        client.merge(user)
        client.commit()


    def delete_user_repository(self, client: SQLAlchemySession, user: UserSchema) -> None:

        client.delete(user)
        client.commit()