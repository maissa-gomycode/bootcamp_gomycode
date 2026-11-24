
import asyncio
import pytest

from app.services import ai


# Test 1 : vérifier le fonctionnement asynchrone

@pytest.mark.asyncio
async def test_async_response(monkeypatch):

    async def fake_call(prompt):
        await asyncio.sleep(0.1)

        return {
            "answer": "Réponse de test",
            "model": "gemini-2.5-flash",
            "tokens_used": 10
        }

    monkeypatch.setattr(ai, "call_llm", fake_call)

    result = await ai.generate_ai_response("Bonjour")

    assert result["answer"] == "Réponse de test"
    assert result["tokens_used"] == 10


# Test 2 : vérifier le timeout

@pytest.mark.asyncio
async def test_timeout(monkeypatch):

    async def slow_call(prompt):
        await asyncio.sleep(2)

        return {
            "answer": "Réponse tardive",
            "model": "gemini-2.5-flash",
            "tokens_used": 10
        }

    monkeypatch.setattr(ai, "call_llm", slow_call)
    monkeypatch.setattr(ai, "TIMEOUT", 0.1)

    with pytest.raises(TimeoutError):

        await ai.generate_ai_response("Test timeout")


# Test 3 : vérifier la gestion des erreurs

@pytest.mark.asyncio
async def test_api_error(monkeypatch):

    async def failing_call(prompt):
        raise RuntimeError("Erreur API simulée")

    monkeypatch.setattr(ai, "call_llm", failing_call)

    with pytest.raises(RuntimeError):

        await ai.generate_ai_response("Test erreur")


# Test 4 : vérifier l'exécution concurrente

@pytest.mark.asyncio
async def test_concurrent_execution():

    async def fake_task(name):

        await asyncio.sleep(1)

        return name

    start = asyncio.get_running_loop().time()

    results = await asyncio.gather(
        fake_task("summary"),
        fake_task("quiz"),
        fake_task("flashcards")
    )

    duration = asyncio.get_running_loop().time() - start

    assert results == [
        "summary",
        "quiz",
        "flashcards"
    ]

    assert duration < 2
