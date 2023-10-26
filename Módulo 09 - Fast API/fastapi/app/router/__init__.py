from fastapi import APIRouter, status, Header
from fastapi.exceptions import HTTPException
import jwt

from app.router import user_routes
from app.configs import jwt_configs

router = APIRouter()

router.include_router(user_routes.router)

@router.get('/', status_code=status.HTTP_200_OK)
def root(authorization_token: str | None = Header(default=None)):
    return checkToken(authorization_token)

def checkToken (token: str):
    payload = jwt.decode(token, jwt_configs["hash_key"], algorithms=["HS256"], verify=True)
    if payload:
        return payload
    return HTTPException(status.HTTP_401_UNAUTHORIZED, "Token is unauthorized")