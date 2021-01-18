from abc import ABCMeta, abstractmethod
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Json
from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError, DatabaseError, DisconnectionError, IntegrityError
from loguru import logger

from ext.database import Base, get_session
from datetime import datetime

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
ResponseCreateType = TypeVar("ResponseCreateType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ResponseUpdateType = TypeVar("ResponseUpdateType", bound=BaseModel)


class CRUDBase(
        Generic[
            ModelType,
            CreateSchemaType,
            ResponseCreateType,
            UpdateSchemaType,
            ResponseUpdateType],
        metaclass=ABCMeta):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update (CRU).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def obj_in_to_db_obj(self, obj_in: Any):
        now = datetime.utcnow()
        obj_in_data = jsonable_encoder(obj_in)
        return self.model(**obj_in_data,
            # audit_date_created = now,
            # audit_date_updated = now,
            # audit_created_by_user_id = requester,
            # audit_updated_by_user_id = requester,
            # audit_deleted = False,
            # audit_date_deleted = None
        )

    @abstractmethod
    async def get(self, id: Any) -> Optional[ModelType]:
        raise NotImplementedError()

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        try:

            response = None
            data_db = self.obj_in_to_db_obj(obj_in=obj_in)
            async with get_session() as db:
                db.add(data_db)
                await db.commit()

            return data_db
        except(DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e

    @abstractmethod
    async def update(
        self,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        raise NotImplementedError()
