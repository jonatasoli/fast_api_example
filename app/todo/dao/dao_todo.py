from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.models_task import Task
from ..schemas.schemas_todo import TaskResponse, TaskBase, TaskCreate, TaskUpdate
from .base import CRUDBase
from ext.database import get_session


class CRUDTask(CRUDBase[
    TaskBase,
    TaskCreate,
    TaskUpdate,
]):
    async def create(self, task_name: TaskCreate, current_user_id: int):

        response = None
        import pdb; pdb.set_trace()

        task_db = self.obj_in_to_db_obj(obj_in=task_name.dict(exclude=current_user_id), requester=current_user_id)
        async with get_session() as db:
            # task_db = Task(**task_name.dict())
            db.add(task_db)
            await db.commit()
            response = TaskResponse.from_orm(task_db)

        return response


task = CRUDTask(Task)
