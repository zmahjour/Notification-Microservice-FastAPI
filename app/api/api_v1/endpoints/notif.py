from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from schemas.notif import EmailSchema
from core.config import settings
from utils.utils import create_otp

