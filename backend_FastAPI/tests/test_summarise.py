
from httpx import AsyncClient, ASGITransport
from app.main import app


async def test_summarise_valid_request():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/summarise",
            json={
                "text": (
                    "FastAPI est un framework Python. "
                    "Il permet de créer des API. "
                    "Pydantic valide les données."
                ),
                "max_bullets": 2
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert len(data["bullets"]) == 2
    assert data["total_bullets"] == 2
