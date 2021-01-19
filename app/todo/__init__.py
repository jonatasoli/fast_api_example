from config import settings
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from todo.api.endpoints import todo_router


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

todo.include_router(todo_router, responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})
