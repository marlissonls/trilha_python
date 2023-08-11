from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass