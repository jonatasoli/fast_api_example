from typing import Optional

from fastapi import FastAPI
from config import settings

from todo import todo


def create_app():
    app = FastAPI()
    app.mount("/todo", todo)
    return app
