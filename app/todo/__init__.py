from config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from todo.api.api_v1.endpoints import todo_router 


todo = FastAPI(
    title=settings.APP_NAME,
    # openapi_url=f"{settings.API_V1_STR}/openapi.json",
    # docs_url=f"{settings.API_V1_STR}",
    # redoc_url=None
)


origins = [
    "*",
]

todo.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todo.include_router(
        todo_router,
        responses={404: {"description": "Not found"}})
