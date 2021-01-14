from typing import Optional

from fastapi import FastAPI
from config import settings

from ext.database import get_engine
from todo import todo


def create_app():
    app = FastAPI()
    app.mount("/todo", todo)
    db = get_engine()
    db.init_app(app)
    return app
