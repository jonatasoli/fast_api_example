from fastapi import status

from todo.schemas.schemas_todo import TaskEndpoint

HEADERS = {"Content-Type": "application/json"}


def test_error_route(client):
    response = client.get(
        "/todo/error_route", headers=HEADERS
    )
    response_data = response.json().get("detail")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_data == "Not Found"


def add_task(client):
    data = TaskEndpoint(name="Task1", completed=False, current_user_id=1)
    response = client.post(
        "/todo/add", headers=HEADERS, json=data.dict()
    )
    return response


def test_add_task(client):
    response = add_task(client)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"name": "Task1", "completed": False, "id": 1}


def test_add_task_error_validate(client):
    """Must be error on validate data"""
    task = {"name": "Task1", "completed": "false"}
    response = client.post(
        "/todo/add", headers=HEADERS, json=task
    )
    response_data = response.json().get("detail")[0]
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_data.get("msg") == "field required"
    assert response_data.get("type") == "value_error.missing"
    assert response_data.get("loc") == ["body", "current_user_id"]


def test_get_task(client):
    response = add_task(client)

    response = client.get(
        f"/todo/get/{response.json()['id']}", headers=HEADERS
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"name": "Task1", "completed": False, "id": 1}


def test_list_tasks():
    ...


def test_update_task(client):
    response = add_task(client)

    new_name = f"{response.json()['id']} Updated"

    data = TaskEndpoint(name=new_name, completed=False, current_user_id=1)
    response = client.put(
        f"/todo/update/{response.json()['id']}", headers=HEADERS, json=data.dict()
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"name": new_name, "completed": False, "id": 1}


def test_delete_task():
    ...
