import uvicorn
from fastapi import FastAPI

from config import settings
from api_v1 import router as v1_router


app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=settings.port,
        workers=settings.workers
    )
