from fastapi import HTTPException, status
from app.repository import UserRepository
from app.base_models import UserIn, UserOut, UserId


class UserService:

    def __init__(self):
        self.repository = UserRepository()


    def create_user_service(self, user: UserIn) -> UserId:

        try:
            result = self.repository.create_user_repository(user)
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Can't create user.")
        else: 
            return result


    def get_user_service(self, user_id: str) -> UserOut:

        try:
            result = self.repository.get_user_repository(user_id)

            if result is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")
        except:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error.")
        else: 
            return result


    def get_users_service(self) -> list[UserOut]:

        try:
            result = self.repository.get_users_repository()

            if result is None:
                print(result)
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        except HTTPException:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users resgistered.")
        else: 
            return result
    

    def update_user_service(self, user_id: str, user: UserIn) -> UserOut:
        
        try:
            result = self.repository.update_user_repository(user_id, user)

            if result is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")
        except:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error.")
        else:
            return result


    def delete_user_service(self, user_id: str) -> None:

        try:
            result = self.repository.delete_user_repository(user_id)
        
            if result is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't find user by id: {user_id}.")
