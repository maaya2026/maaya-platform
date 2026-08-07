from fastapi.testclient import TestClient

from maaya.main import app

client = TestClient(app)


def test_root_identifies_maaya() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "MAAYA Platform"
    assert response.json()["version"] == "0.1.0"


def test_health_endpoint_reports_healthy() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "healthy"
    assert payload["service"] == "MAAYA Platform"
    assert payload["version"] == "0.1.0"
    assert payload["timestamp"]


def test_readiness_endpoint_reports_ready() -> None:
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ready"
