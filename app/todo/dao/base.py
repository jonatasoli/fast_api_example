from abc import ABCMeta, abstractmethod
from typing import Any, Dict, Generic, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.exc import DataError, DatabaseError, DisconnectionError, IntegrityError
from loguru import logger

from ext.database import Base, get_session
from datetime import datetime

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=ABCMeta
):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update (CRU).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def obj_in_to_db_obj(self, obj_in: Any):
        obj_in_data = jsonable_encoder(obj_in)
        user_id = obj_in_data.pop("current_user_id")
        return self.model(**obj_in_data, created_by_id=user_id, updated_by_id=user_id)

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
                response = self.Meta.ResponseCreateType.from_orm(data_db)

            return response
        except (DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e

    @abstractmethod
    async def update(
        self, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        raise NotImplementedError()
