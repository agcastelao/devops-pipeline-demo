from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_status_endpoint_returns_ok():
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "uptime" in data
    assert isinstance(data["uptime"], float)
