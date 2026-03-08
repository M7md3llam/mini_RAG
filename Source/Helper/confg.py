from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    APP_NAME: str 
    APP_VERSION: str 
    API_KEY: str
    FILE_ALLOWED_EXTENSIONS: list
    FILE_SIZE: int

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
