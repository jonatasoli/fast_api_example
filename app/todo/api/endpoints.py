from fastapi import APIRouter, status
from loguru import logger
from todo.bootstrap import bootstrap

from todo.schemas.schemas_todo import TaskCreate, TaskCreateResponse, TaskGetResponse, TaskUpdate, TaskUpdateResponse
from todo.services import services_todo

todo_router = APIRouter()

bootstrap = bootstrap()


@todo_router.post('/add', status_code=status.HTTP_201_CREATED, response_model=TaskCreateResponse)
async def add_task(*, task_data: TaskCreate):
    try:
        return await services_todo.add_task(uow=bootstrap.uow, task_data=task_data)
    except Exception as e:
        logger.error(f'Error return endpoint {e}')
        raise e


@todo_router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=TaskUpdateResponse)
async def update_task(*, id: int, data: TaskUpdate):
    try:
        return await services_todo.update_task(id, data, uow=bootstrap.uow)
    except Exception as e:
        logger.error(f'Error return endpoint {e}')
        raise e


@todo_router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=TaskGetResponse)
async def get_task(*, id: int):
    try:
        return await services_todo.get_task(id, uow= bootstrap.uow)
    except Exception as e:
        logger.error(f'Error return endpoint {e}')
        raise e
