def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_task(client):
    response = client.post("/tasks/", json={
        "title": "Test task",
        "description": "Test description"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test task"
    assert data["completed"] == False

def test_get_all_tasks(client):
    client.post("/tasks/", json={"title": "Task 1"})
    client.post("/tasks/", json={"title": "Task 2"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_task_by_id(client):
    created = client.post("/tasks/", json={"title": "My task"})
    task_id = created.json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "My task"

def test_update_task(client):
    created = client.post("/tasks/", json={"title": "Old title"})
    task_id = created.json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] == True

def test_delete_task(client):
    created = client.post("/tasks/", json={"title": "Delete me"})
    task_id = created.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_task_not_found(client):
    response = client.get("/tasks/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"