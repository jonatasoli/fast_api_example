from fastapi import Header, APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from loguru import logger

from ext.database import get_session
from todo.schemas.schemas_todo import Task
from todo.services import services_todo

todo_router = APIRouter()


@todo_router.post('/add', status_code=201)
async def add_task(
        *,
        task_data: Task
        ):
    return services_todo.add_task(task_data)
