from pydantic import BaseModel


class Task(BaseModel):
    name: str
    completed: bool

class TaskResponse(Task):
    id: int
