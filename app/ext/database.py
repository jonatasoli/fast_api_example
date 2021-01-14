from typing import Any

from gino.ext.starlette import Gino
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from config import settings


def get_engine():
    """'postgresql://scott:tiger@localhost:5432/mydatabase'"""
    return Gino(
        dsn=settings.DB_DSN,
        pool_min_size=settings.DB_POOL_MIN_SIZE,
        pool_max_size=settings.DB_POOL_MAX_SIZE,
        echo=settings.DB_ECHO,
        ssl=settings.DB_SSL,
        use_connection_for_request=settings.DB_USE_CONNECTION_FOR_REQUEST,
        retry_limit=settings.DB_RETRY_LIMIT,
        retry_interval=settings.DB_RETRY_INTERVAL,
    )


# def get_session():
#     return Gino(
#         dsn=settings.DB_DSN,
#         pool_min_size=settings.DB_POOL_MIN_SIZE,
#         pool_max_size=settings.DB_POOL_MAX_SIZE,
#         echo=settings.DB_ECHO,
#         ssl=settings.DB_SSL,
#         use_connection_for_request=settings.DB_USE_CONNECTION_FOR_REQUEST,
#         retry_limit=settings.DB_RETRY_LIMIT,
#         retry_interval=settings.DB_RETRY_INTERVAL,
#     )


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

db = get_engine()
