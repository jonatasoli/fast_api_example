from fastapi import APIRouter, status
from loguru import logger

from todo.schemas.schemas_todo import TaskEndpoint
from todo.services import services_todo

todo_router = APIRouter()


@todo_router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_task(*, data: TaskEndpoint):
    try:
        return await services_todo.add_task(data)
    except Exception as e:
        logger.error(f"Error return endpoint {e}")
        raise e


@todo_router.put("/update/{id}", status_code=status.HTTP_200_OK)
async def update_task(*, id: int, data: TaskEndpoint):
    try:
        return await services_todo.update_task(id, data)
    except Exception as e:
        logger.error(f"Error return endpoint {e}")
        raise e


@todo_router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def update_task(*, id: int):
    try:
        return await services_todo.get_task(id)
    except Exception as e:
        logger.error(f"Error return endpoint {e}")
        raise e
