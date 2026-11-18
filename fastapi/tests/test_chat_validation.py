
import pytest

from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_chat_missing_message_returns_422():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={}
        )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_chat_empty_message_returns_400():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={"message": "   "}
        )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_chat_message_too_long_returns_422():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={"message": "A" * 2001}
        )

    assert response.status_code == 422
