from pydantic import BaseModel


class TaskInDB(BaseModel):
    name: str
    completed: bool

    class Config:
        orm_mode = True


class TaskResponse(TaskInDB):
    id: int

    class Config:
        orm_mode = True
