from fastapi import FastAPI, status
from app.router import user_routes
from app.middlewares import BaseHTTPMiddleware, db_session_middleware

api = FastAPI()

api.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)

api.include_router(user_routes.router)

@api.get('/', status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello! Try /user"}