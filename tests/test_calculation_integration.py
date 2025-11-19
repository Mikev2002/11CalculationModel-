def test_create_calculation_add(client):
    payload = {"a": 5, "b": 7, "type": "Add"}
    response = client.post("/calculate", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["a"] == 5
    assert data["b"] == 7
    assert data["type"] == "Add"
    assert data["result"] == 12


def test_create_calculation_divide(client):
    payload = {"a": 10, "b": 2, "type": "Divide"}
    response = client.post("/calculate", json=payload)

    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_create_calculation_invalid_type(client):
    payload = {"a": 5, "b": 5, "type": "Invalid"}
    response = client.post("/calculate", json=payload)

    assert response.status_code == 422  # Pydantic reject
