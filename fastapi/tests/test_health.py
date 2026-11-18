
import pytest

from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_health_endpoint_returns_ok():

    # Permet de tester FastAPI directement
    transport = ASGITransport(app=app)

# permet d'envoyer des requêtes HTTP asynchrones.
    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        # Envoie une requête GET
        response = await client.get("/health")

    # Vérifie le code HTTP
    assert response.status_code == 200

    # Récupère le JSON
    data = response.json()

    # Vérifie les données retournées
    assert data["status"] == "ok"
    assert "message" in data
