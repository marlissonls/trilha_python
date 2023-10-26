from fastapi import FastAPI, status
from app.router import user

api = FastAPI()

api.include_router(user.router)

@api.get('/', status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello! Try /user"}