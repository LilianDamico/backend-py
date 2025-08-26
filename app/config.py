from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_PORT: int = 8080
    DATABASE_URL: str
    REMOTIVE_BASE: str = "https://remotive.com/api"

    class Config:
        env_file = ".env"

settings = Settings()
