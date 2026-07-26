from fastapi.testclient import TestClient

from backend.app.main import app

from pathlib import Path

client = TestClient(app)

def test_predict_without_file():

    response = client.post(
        "/version2/predict"
    )

    assert response.status_code == 422




def test_predict_invalid_extension():

    response = client.post(
        "/version2/predict",
        files={
            "file": (
                "invalid.pdf",
                b"dummy content",
                "application/pdf"
            )
        }
    )

    assert response.status_code == 400




def test_predict_empty_csv():

    response = client.post(
        "/version2/predict",
        files={
            "file": (
                "empty.csv",
                b"",
                "text/csv"
            )
        }
    )

    assert response.status_code == 400





def test_predict_invalid_column_count():

    csv_data = (
        "engine_id,cycle,sensor_1\n"
        "1,1,100\n"
    )

    response = client.post(
        "/version2/predict",
        files={
            "file": (
                "invalid.csv",
                csv_data,
                "text/csv"
            )
        }
    )

    assert response.status_code == 400








def test_predict_valid_dataset():

    demo_file = (
        Path("DATA")
        / "demo"
        / "Engine1_60.csv"
    )

    with open(demo_file, "rb") as f:

        response = client.post(
            "/version2/predict",
            files={
                "file": (
                    "Engine1_60.csv",
                    f,
                    "text/csv",
                )
            },
        )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200

    data = response.json()

    assert "total_engines" in data
    assert "predictions" in data
    assert len(data["predictions"]) > 0

    prediction = data["predictions"][0]

    assert "engine_id" in prediction
    assert "predicted_rul" in prediction
    assert "risk" in prediction
    assert "recommendation" in prediction