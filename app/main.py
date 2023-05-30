from fastapi import FastAPI

from todo import todo


def create_app():
    app = FastAPI()
    app.mount('/todo', todo)
    return app
