from fastapi import APIRouter
from app.schemas.auth import LoginRequest, LoginResponse, UserPublic

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def fake_login(data: LoginRequest):
    # respuesta simulada para pruebas
    fake_user = UserPublic(
        id=1,
        email=data.email,
        rol="USER"
    )

    return LoginResponse(
        access_token="fake-token",
        user=fake_user
    )
