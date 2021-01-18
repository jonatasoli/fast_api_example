from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    completed: bool


class TaskCreate(TaskBase):
    ...

class TaskUpdate(TaskBase):
    ...


class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskEndpoint(TaskBase):
    current_user_id: int
