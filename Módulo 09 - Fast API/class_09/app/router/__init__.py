from app.base_models import UserIn, UserOut, UserId
from app.controller import UserController
from fastapi import FastAPI, status
from typing import Any

api = FastAPI()

controller = UserController()


@api.post('/user/', status_code=status.HTTP_201_CREATED, response_model=UserId)
def create_user(user: UserIn) -> Any:

    result = controller.create_user_controller(user)

    return result


@api.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=UserOut)
def get_users(user_id: str) -> Any:

    result = controller.get_user_controller(user_id)

    return result


@api.get('/users/', status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users() -> Any:

    result = controller.get_users_controller()

    return result


@api.put('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=UserOut)
def update_user(user_id: str, user: UserIn) -> Any:

    result = controller.update_user_controller(user_id, user)

    return result


@api.delete('/user/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_users(user_id: str) -> None:

    controller.delete_user_controller(user_id)