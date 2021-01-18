from abc import ABCMeta
from typing import Any, Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from loguru import logger
from pydantic import BaseModel
from sqlalchemy.exc import DataError, DatabaseError, DisconnectionError, IntegrityError

from ext.database import Base, get_session

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

    async def get(self, id: Any):
        try:
            async with get_session() as db:
                return db.query(self.model).get(id)

        except (DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e

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

    async def update(self, id: Any, obj_in: UpdateSchemaType) -> ModelType:
        try:
            db_obj = await self.get(id)
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            # db.add(db_obj)
            # db.commit()
            # db.refresh(db_obj)
            return db_obj
        except (DataError, DatabaseError, DisconnectionError, IntegrityError) as err:
            logger.error(f"SQLAlchemy error {err}")
        except Exception as e:
            logger.error(f"Error in dao {e}")
            raise e
