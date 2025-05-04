import pytest
import responses
import httpx

from pricefinder.cores.req_handler import RequestHandler


@pytest.fixture
def handler():
    return RequestHandler(timeout=5)


@responses.activate
def test_get_request(handler):
    responses.add(
        responses.GET,
        "https://example.com",
        json={"message": "ok"},
        status=200
    )

    response = handler._get("https://example.com")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}


@responses.activate
def test_post_request(handler):
    responses.add(
        responses.POST,
        "https://example.com",
        json={"result": "success"},
        status=201
    )

    response = handler._post("https://example.com", json={"key": "value"})
    assert response.status_code == 201
    assert response.json()["result"] == "success"


@pytest.mark.asyncio
async def test_async_get(monkeypatch):
    async def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
            async def aclose(self): pass
            def json(self): return {"data": "ok"}
        return MockResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    handler = RequestHandler()
    response = await handler._aget("https://example.com")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_async_post(monkeypatch):
    async def mock_post(*args, **kwargs):
        class MockResponse:
            status_code = 200
            async def aclose(self): pass
            def json(self): return {"data": "posted"}
        return MockResponse()

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    handler = RequestHandler()
    response = await handler._apost("https://example.com", json={"key": "val"})
    assert response.status_code == 200
