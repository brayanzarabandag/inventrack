from pydantic import BaseModel, EmailStr
from typing import Optional

# Usuario público (resumen)

class UserPublic(BaseModel):
    id: int
    email: EmailStr
    rol: str

# Login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserPublic

# Token interno para JWT
class TokenData(BaseModel):
    user_id: Optional[int] = None
    rol: Optional[str] = None

# Recuperación de contraseña
class PasswordRecoveryRequest(BaseModel):
    email: EmailStr

class PasswordResetRequest(BaseModel):
    token: str
    new_password: str