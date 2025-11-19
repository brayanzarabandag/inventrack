from pydantic import BaseSettings

class Settings(BaseSettings):
    env: str = "development"
    secret_key: str
    jwt_secret_key: str
    access_token_expire_minutes: int = 60
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()