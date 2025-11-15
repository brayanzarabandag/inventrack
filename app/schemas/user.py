from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    nombre: str
    rol: str        # "ADMIN" o "USER"
    activo: Optional[bool] = True
    password: str


# LO QUE SE DEVUELVE AL CLIENTE
class UserPublic(BaseModel):
    id: int
    email: EmailStr
    nombre: str
    rol: str
    activo: bool


# MODELO INTERNO (contraseña hasheada)
class UserInDB(BaseModel):
    id: int
    email: EmailStr
    nombre: str
    rol: str
    activo: bool
    password_hash: str
