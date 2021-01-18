from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import DataError, DatabaseError, DisconnectionError, IntegrityError
from loguru import logger

from ..models.models_task import Task
from ..schemas.schemas_todo import (
    TaskCreateResponse,
    TaskUpdateResponse,
    TaskBase,
    TaskCreate,
    TaskUpdate,
)
from .base import CRUDBase
from ext.database import get_session


class CRUDTask(
    CRUDBase[
        TaskBase,
        TaskCreate,
        TaskUpdate,
    ]
):
    class Meta:
        ResponseCreateType = TaskCreateResponse
        ResponseUpdateType = TaskUpdateResponse
        ResponseGetType = None

    async def update(self, task_model: Task, task_schema: TaskUpdate):
        try:
            return True
        except (DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e

    async def get(self, id):
        try:
            async with get_session() as db:
                return db.query(self.model).get(id)

        except (DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e
