from .base import CRUDBase
from ..schemas.schemas_todo import (
    TaskCreateResponse,
    TaskUpdateResponse,
    TaskBase,
    TaskCreate,
    TaskUpdate,
)


class CRUDTask(
    CRUDBase[
        TaskBase,
        TaskCreate,
        TaskUpdate,
    ]
):
    class Meta:
        ResponseCreateType = TaskCreateResponse
        ResponseUpdateType = TaskUpdateResponse
        ResponseGetType = None
