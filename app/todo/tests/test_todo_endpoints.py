import pytest
from unittest import mock
from todo.schemas.schemas_todo import TaskEndpoint
from loguru import logger


def test_add_task(client):
    data = TaskEndpoint(name="Task1", completed=False, current_user_id=1)
    response = client.post(
        "/todo/add", headers={"Content-Type": "application/json"}, json=data.dict()
    )
    logger.debug(f"------------ {response} ----------")
    logger.debug(f"------------ {response.content} ----------")
    assert response.status_code == 201


def test_list_tasks():
    ...


def test_list_task():
    ...


def test_update_task():
    ...


def test_delete_task():
    ...
