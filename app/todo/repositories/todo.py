import abc
from sqlalchemy import select, between

from todo.models.models_todo import Task
from todo.schemas.schemas_todo import TaskCreateResponse, TaskUpdateResponse
from util import obj_in_to_db_obj


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: Task):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Task:
        raise NotImplementedError


class qlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    async def add(self, todo):
        db_todo = Task(
            name=todo.name,
            completed=todo.completed,
        )
        async with self.session.begin() as session:
            session.add(db_todo)
            await session.flush()
            await session.refresh(db_todo)
        return TaskCreateResponse.from_orm(db_todo)

    async def get(self, id):
        smtm = select(Task).where(Task.id==id)
        _result = await self.session.execute(smtm)
        return _result.scalars().first()

    async def update_task(self, id, todo):
        smtm = select(Task).where(Task.id==id)
        async with self.session.begin() as session:
            _result = await session.execute(smtm)
            _result_update = session.add(
                Task(
                    id=_result.id,
                    name=todo.name,
                    completed=todo.completed,
                )
            )
        return _result_update.scalars().first()
