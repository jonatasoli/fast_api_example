import pytest
from unittest import mock
from todo.schemas.schemas_todo import TaskEndpoint, TaskCreate
from loguru import logger
from fastapi import status


def test_error_route(client):
    response = client.get("/todo/error_route", headers={"Content-Type": "application/json"})
    response_data = response.json().get("detail")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_data == "Not Found"


def test_add_task(client):
    data = TaskEndpoint(name="Task1", completed=False, current_user_id=1)
    response = client.post("/todo/add", headers={"Content-Type": "application/json"}, json=data.dict())
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"name": "Task1", "completed": False, "id": 1}


def test_add_task_error_validate(client):
    """Must be error on validate data"""
    task = {"name": "Task1", "completed": "false"}
    response = client.post("/todo/add", headers={"Content-Type": "application/json"}, json=task)
    response_data = response.json().get("detail")[0]
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_data.get("msg") == "field required"
    assert response_data.get("type") == "value_error.missing"
    assert response_data.get("loc") == ["body", "current_user_id"]


def test_list_tasks():
    ...


def test_list_task():
    ...


def test_update_task():
    ...


def test_delete_task():
    ...
