
from httpx import AsyncClient, ASGITransport
from app.main import app


async def test_quiz_valid_request():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/quiz",
            json={
                "topic": "Python",
                "num_questions": 3
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert data["topic"] == "Python"
    assert data["total_questions"] == 3
    assert len(data["questions"]) == 3


async def test_quiz_too_many_questions():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/quiz",
            json={
                "topic": "Python",
                "num_questions": 50
            }
        )

    assert response.status_code == 422
