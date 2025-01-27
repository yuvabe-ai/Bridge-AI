from typing import Optional
from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    name: str
    email: str

class UpdateUserSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None