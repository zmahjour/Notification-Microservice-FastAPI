from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from schemas.notif import EmailSchema
from core.config import settings
from utils.utils import create_otp


router = APIRouter(prefix="/notif", tags=["notification"])


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    VALIDATE_CERTS=settings.VALIDATE_CERTS,
)


@router.post("/email", status_code=status.HTTP_200_OK)
async def send_email(request: Request, email: EmailSchema) -> JSONResponse:
    otp = create_otp()
    text = f"OTP Code: {otp}"
    redis = request.app.state.redis
    email = email.model_dump().get("email")

    message = MessageSchema(
        subject="Notification",
        recipients=email,
        body=text,
        subtype=MessageType.plain,
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    await redis.set(email[0], otp, settings.OTP_EXPIRE_TIME)

    return {"detail": "Email has been sent."}
