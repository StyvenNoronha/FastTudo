from fastapi import FastAPI # type: ignore
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_models import User
from models.task_model import Task
from api.api_v1.router import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.on_event("startup")
async def app_init():
    cliente_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING).todoapp
    
    await init_beanie(
        database = cliente_db,
        document_models = [
            User,
            Task
        ]
    )

app.include_router(
    router,
    prefix=settings.API_V1_STR
)    