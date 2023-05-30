from __future__ import annotations
import abc
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from todo import repository
from config import settings



class AbstractUnitOfWork(abc.ABC):
    todo: repository.AbstractRepository

    async def __aenter__(self) -> AbstractUnitOfWork:
        return self

    async def __aexit__(self, *args):
        await self.rollback()

    async def commit(self):
        await self._commit()

    @abc.abstractmethod
    async def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def rollback(self):
        raise NotImplementedError


def session_factory():
    if not hasattr(settings, "DB_DSN"):
        return None
    return sessionmaker(
        expire_on_commit=False,
        class_=AsyncSession,
        bind=create_async_engine(
            settings.DB_DSN,
        )
    )


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=session_factory()):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()  # type: Session
        self.todo = repository.SqlAlchemyRepository(self.session)
        return super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def _commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
