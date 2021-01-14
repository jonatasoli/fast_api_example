from pydantic import BaseModel


class Task(BaseModel):
    name: str
    completed: bool

    class Config:
        orm_mode = True


class TaskResponse(Task):
    id: int
