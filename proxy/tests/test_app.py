from fastapi.testclient import TestClient
from http import HTTPStatus
from proxy.app import app
from proxy.tests.test_data import TEST_PAYLOAD, NUMBER_OF_REQUESTS

client = TestClient(app)


def test_proxy():
    response = client.post("/proxy", json=TEST_PAYLOAD)
    assert response.status_code == HTTPStatus.OK
    assert "x-my-jwt" in response.headers


def test_status():
    response = client.get("/status")
    assert response.status_code == HTTPStatus.OK
    assert "time_from_start" in response.json()
    assert "number_of_requests" in response.json()


def test_number_of_requests():
    first_response = client.get("/status")
    assert first_response.status_code == HTTPStatus.OK
    initial_number_of_requests = first_response.json()["number_of_requests"]

    for _ in range(NUMBER_OF_REQUESTS):
        client.post("/proxy", json=TEST_PAYLOAD)

    second_response = client.get("/status")
    assert second_response.status_code == HTTPStatus.OK
    assert second_response.json()["number_of_requests"] == initial_number_of_requests + NUMBER_OF_REQUESTS
