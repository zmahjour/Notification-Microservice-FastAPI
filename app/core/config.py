from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # E-Mail
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    VALIDATE_CERTS: bool

    # OTP
    OTP_EXPIRE_TIME: int = 120


    class Config:
        env_file = (
            "/home/samane/Documents/MaktabSharif/FinalProject/Project/Notification/.env"
        )


settings = Settings()
