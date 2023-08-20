from app.database import DATABASE_PATH
from app.repository import UserRepository
from app.service import UserService
from app.controller import UserController
from app.user_interfaces.user_models import UserIn, UserOut, UserId
from fastapi import APIRouter, status
from typing import Any


database = DATABASE_PATH
repository = UserRepository(database)
service = UserService(repository)
controller = UserController(service)


router = APIRouter(prefix="/user", tags=["user"])

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserId)
def create_user(user: UserIn) -> Any:

    result = controller.create_user_controller(user)

    return result


@router.get('/id/{user_id}', status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user_by_id(user_id: str) -> Any:
    print(user_id)
    result = controller.get_user_by_id_controller(user_id)

    return result


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users() -> Any:

    result = controller.get_users_controller()

    return result


@router.get('/index/{index}', status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user_by_index(index: str) -> Any:

    result = controller.get_user_by_index_controller(index)

    return result


@router.put('/{user_id}', tags=['custom'], status_code=status.HTTP_200_OK, response_model=UserOut)
def update_user(user_id: str, user: UserIn) -> Any:

    result = controller.update_user_controller(user_id, user)

    return result


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str) -> None:

    controller.delete_user_controller(user_id)