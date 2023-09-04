from app.repository.user.sqlalchemy import UserRepository
from app.repository.user.service import UserService
from app.repository.user.controller import UserController
from app.repository.user.models.user_models import UserIn, UserOut, UserId, UserForm
from fastapi import APIRouter, Form, File, UploadFile, status
from typing import Any, Annotated


repository = UserRepository()
service = UserService(repository)
controller = UserController(service)


router = APIRouter(prefix="/user", tags=["user"])


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user_by_id(user_id: str) -> Any:
    return controller.get_user_by_id_controller(user_id)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users() -> Any:
    return controller.get_users_controller()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserId)
def create_user(
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
    profile_image: Annotated[UploadFile, File()]
) -> Any:
    return controller.create_user_controller(
        name,
        email,
        password,
        profile_image
    )


@router.post('/checkuser', status_code=status.HTTP_200_OK, response_model=UserOut)
def check_user(form: UserForm) -> Any:
    return controller.check_user_controller(form)


@router.put('/{user_id}', tags=['custom'], status_code=status.HTTP_200_OK, response_model=UserOut)
def update_user(user_id: str, user: UserIn) -> Any:
    return controller.update_user_controller(user_id, user)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str) -> None:
    controller.delete_user_controller(user_id)