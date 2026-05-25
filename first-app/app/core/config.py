from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    SECRET_KEY: str = "default_secret"

    class Config:
        env_file = ".env"

settings = Settings()
