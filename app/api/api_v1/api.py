from fastapi import APIRouter
from .endpoints.notif import router as notif_router


router = APIRouter()
router.include_router(notif_router)
