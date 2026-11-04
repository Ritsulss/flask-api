import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_get_hello_returns_welcome_message(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"message": "Welcome to the Flask API!"}


def test_post_hello_greets_by_name(client):
    response = client.post("/hello", json={"name": "  Ada  "})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Ada!"}


@pytest.mark.parametrize("body", [{}, {"name": ""}, {"name": "   "}, {"name": 42}, []])
def test_post_hello_rejects_invalid_body(client, body):
    response = client.post("/hello", json=body)
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_get_data_returns_sample_items(client):
    response = client.get("/data")
    body = response.get_json()
    assert response.status_code == 200
    assert body["count"] == 3
    assert len(body["items"]) == 3
    assert set(body["items"][0]) == {"id", "name", "category"}


def test_post_data_creates_item_and_it_can_be_read_back(client):
    response = client.post("/data", json={"name": "Mouse", "category": "electronics"})
    assert response.status_code == 201
    assert response.get_json() == {"id": 4, "name": "Mouse", "category": "electronics"}

    body = client.get("/data").get_json()
    assert body["count"] == 4
    assert body["items"][-1]["name"] == "Mouse"


@pytest.mark.parametrize(
    "body, missing",
    [
        ({"category": "electronics"}, "name"),
        ({"name": "Mouse"}, "category"),
        ({"name": "Mouse", "category": 7}, "category"),
    ],
)
def test_post_data_reports_invalid_fields(client, body, missing):
    response = client.post("/data", json=body)
    assert response.status_code == 400
    assert missing in response.get_json()["error"]
    assert client.get("/data").get_json()["count"] == 3


def test_post_data_rejects_malformed_json(client):
    response = client.post("/data", data="{not json", content_type="application/json")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_post_data_rejects_non_json_content_type(client):
    response = client.post("/data", data="name=Mouse")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_unknown_route_returns_json_404(client):
    response = client.get("/missing")
    assert response.status_code == 404
    assert response.is_json


def test_unsupported_method_returns_json_405(client):
    response = client.delete("/hello")
    assert response.status_code == 405
    assert response.is_json


def test_each_app_starts_with_fresh_data():
    first = create_app().test_client()
    first.post("/data", json={"name": "Mouse", "category": "electronics"})
    second = create_app().test_client()
    assert second.get("/data").get_json()["count"] == 3
