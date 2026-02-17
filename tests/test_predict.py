from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_predict_endpoint():
    payload = {
        "text": "Python developer with FastAPI and Docker experience"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "skills_found" in data
    assert "skills_count" in data
    assert data["skills_count"] == len(data["skills_found"])
