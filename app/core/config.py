from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = (
            "/home/samane/Documents/MaktabSharif/FinalProject/Project/Notification/.env"
        )


