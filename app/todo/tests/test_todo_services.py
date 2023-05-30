from unittest import mock

import pytest

from todo.schemas.schemas_todo import (TaskCreate, TaskCreateResponse,
                                       TaskEndpoint)
from todo.services.services_todo import add_task

response_obj = TaskCreateResponse(id=1, name='Task 1', completed=False)


@pytest.mark.asyncio
@mock.patch('todo.dao.task.create', return_value=response_obj)
async def test_add_task(mocker):
    data = TaskEndpoint(name='Task 1', completed=False, current_user_id=1)
    response = await add_task(task_data=data)
    assert response == response_obj
