from .base import CRUDBase
from todo.schemas.schemas_todo import (
    TaskCreateResponse,
    TaskUpdateResponse,
    TaskGetResponse,
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
        response_create_type = TaskCreateResponse
        response_update_type = TaskUpdateResponse
        response_get_type = TaskGetResponse
