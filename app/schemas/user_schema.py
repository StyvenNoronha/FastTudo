from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description='Email do Usuário')
    username: str = Field(...,min_length=5,max_length=50, description='Username')
    password: str = Field(...,min_length=5,max_length=50, description='Senha do Usuario')


class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: str    
    