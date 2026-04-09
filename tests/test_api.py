from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    assert client.get("/").status_code == 200

def test_prediction():
    response = client.post("/predict", json={
        "age": 40,
        "blood_pressure": 120,
        "cholesterol": 200
    })
    assert response.status_code == 200
    assert "prediction" in response.json()
