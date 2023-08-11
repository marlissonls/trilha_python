from pydantic import BaseModel, EmailStr

class HomePage(BaseModel):
    get_users: str

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass