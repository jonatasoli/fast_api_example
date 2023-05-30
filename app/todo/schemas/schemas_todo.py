from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    completed: bool


class TaskCreate(TaskBase):
    ...


class TaskCreateResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskUpdate(TaskBase):
    ...


class TaskUpdateResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskGetResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True
