from fastapi import Header, APIRouter, Depends, status
from fastapi.responses import JSONResponse

from loguru import logger

from todo.schemas.schemas_todo import TaskInDB
from todo.services import services_todo

todo_router = APIRouter()


@todo_router.post("/add", status_code=201)
async def add_task(*, task_data: TaskInDB):
    return await services_todo.add_task(task_data)
