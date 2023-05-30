import abc
from sqlalchemy import select, between
from sqlalchemy.engine import result

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


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    async def add(self, todo):
        db_todo = Task(
            name=todo.name,
            completed=todo.completed,
        )
        self.session.add(db_todo)
        await self.session.flush()
        return db_todo

    async def get(self, id):
        smtm = select(Task).where(Task.id==id)
        _result = await self.session.execute(smtm)
        return _result.scalars().first()

    async def update_task(self, id, todo):
        smtm = select(Task).where(Task.id==id)
        async with self.session.begin() as session:
            _result = await self.session.execute(smtm)
            _result_update = _result.scalars().first()
            _result_update.name = todo.name
            _result_update.completed = todo.completed
            self.session.add(_result_update)
        await self.session.flush()
        return _result_update
