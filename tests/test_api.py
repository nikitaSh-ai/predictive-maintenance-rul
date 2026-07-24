from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)

def test_predict_without_file():

    response = client.post(
        "/version2/predict"
    )

    assert response.status_code == 422