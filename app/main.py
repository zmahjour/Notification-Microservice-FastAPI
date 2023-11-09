from fastapi import FastAPI
import uvicorn
from api.api_v1.api import router as notif_router


app = FastAPI()
app.include_router(notif_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
