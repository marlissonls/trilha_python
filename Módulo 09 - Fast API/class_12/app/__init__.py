from fastapi import FastAPI, status
from app.router import user_routes

api = FastAPI()

api.include_router(user_routes.router)

@api.get('/', status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello! Try /user"}