from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.models_task import Task
from ..schemas.schemas_todo import TaskResponse, TaskInDB
from ext.database import get_session


async def addTask(task_name):

    response = None
    async with get_session() as db:
        task_db = Task(**task_name.dict())
        db.add(task_db)
        await db.commit()
        response = TaskResponse.from_orm(task_db)

    return response
