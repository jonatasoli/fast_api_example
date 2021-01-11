from typing import Optional

from fastapi import FastAPI
from config import settings

from ext.database import get_engine
from todo import todo


# app = FastAPI(
#     title=settings.APP_NAME,
#     openapi_url=f"{settings.MAIN_APP}/openapi.json",
#     docs_url=f"/{settings.MAIN_APP}",
#     redoc_url=None)
app = FastAPI()
app.mount("/todo", todo)
db = get_engine()
db.init_app(app)

# def get_app():
#     app.mount('/todo', todo)
#     db = get_engine()
#     db.init_app(app)
#     return app

