from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import aioredis
from api.api_v1.api import router as notif_router
from core.config import settings



app = FastAPI()
app.include_router(notif_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
