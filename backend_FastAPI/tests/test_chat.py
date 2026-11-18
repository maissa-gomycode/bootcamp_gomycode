
from httpx import AsyncClient, ASGITransport
from app.main import app


async def test_chat_valid_message():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={
                "message": "Explique FastAPI"
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "model" in data
    assert "tokens_used" in data


async def test_chat_missing_message():

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


async def test_chat_empty_message():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={"message": "   "}
        )

    assert response.status_code == 422
