import pytest
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_tasks_data = {
            "title": "Nova tarefa",
            "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/Tasks", json=new_tasks_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/Tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "Tasks" in response_json
    assert "Total_tasks"

def test_get_task():
    if tasks:
        Task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/Tasks/{Task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert Task_id == response_json['id']

def test_update_task():
    if tasks:
        Task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Titulo Atualizado"
        }
        response = requests.put(f"{BASE_URL}/Tasks/{Task_id}", json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Nova requisição a tarefa especifica
        response = requests.get(f"{BASE_URL}/Tasks/{Task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]

def test_delete_tasks():
    if tasks:
        Task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/Tasks/{Task_id}")
        response.status_code == 200

        response = requests.get(f"{BASE_URL}/Tasks/{Task_id}")
        assert response.status_code == 404