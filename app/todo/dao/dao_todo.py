from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import DataError, DatabaseError, DisconnectionError, IntegrityError
from loguru import logger

from ..models.models_task import Task
from ..schemas.schemas_todo import TaskCreateResponse, TaskUpdateResponse, TaskBase, TaskCreate, TaskUpdate, Validation
from .base import CRUDBase
from ext.database import get_session


class CRUDTask(CRUDBase[
    TaskBase,
    TaskCreate,
    TaskCreateResponse,
    TaskUpdate,
    TaskUpdateResponse,
]):
    async def create(self, obj_in: TaskCreate):
        db_data = await super().create(obj_in)
        return TaskCreateResponse.from_orm(db_data)
    # async def create(self, obj_in: TaskCreate, validation: Validation):
    #     try:

    #         response = None

    #         task_db = self.obj_in_to_db_obj(obj_in=task, requester=validation.current_user_id)
    #         async with get_session() as db:
    #             db.add(task_db)
    #             await db.commit()
    #             response = TaskCreateResponse.from_orm(task_db)

    #         return response
    #     except(DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
    #         logger.error(f"SQLAlchemy error {err}")
    #     except Exception as e:
    #         logger.error(f"Error in dao {e}")
    #         raise e

    async def update(self, task_model: Task, task_schema: TaskUpdate):
        try:
            return True
        except(DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e

    async def get(self, id):
        try:
            async with get_session() as db:
                return db.query(self.model).get(id)

        except(DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e
