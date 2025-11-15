from fastapi import APIRouter
from app.schemas.user import UserCreate, UserPublic, UserUpdate, UserInDB

router = APIRouter()

@router.post("/", response_model=UserPublic)
def fake_create_user(user: UserCreate):
    return UserPublic(
        id=1,
        email=user.email,
        nombre=user.nombre,
        rol=user.rol,
        activo=user.activo
    )

@router.get("/{user_id}", response_model=UserPublic)
def fake_get_user(user_id: int):
    return UserPublic(
        id=user_id,
        email="test@example.com",
        nombre="Usuario Prueba",
        rol="USER",
        activo=True
    )
