from sqlalchemy.engine.url import URL, make_url
from starlette.datastructures import Secret
from gino.ext.starlette import Gino

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


def get_session():
    _engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    try:
        yield db
    finally:
        db.close()


class Base:
    ...
