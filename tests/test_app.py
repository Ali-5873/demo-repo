from app import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from Flask Redis GitOps API"


def test_health_route_returns_json():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code in [200, 500]

    data = response.get_json()
    assert "status" in data
    assert "redis" in data