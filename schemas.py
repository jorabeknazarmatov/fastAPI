from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str = Field(max_length=100)
    email: EmailStr = Field(max_length=200)

class EditName(BaseModel):
    id: int 
    name: str = Field(max_length=100)


class Post(BaseModel):
    user_id: int
    title: str = Field(max_length=300)
    content: str = Field(max_length=1000)