
from app.cache.redis_cache import (
    get_cached_response,
    set_cached_response
)

question = "Qu'est-ce que Python ?"

# Première consultation
response = get_cached_response(question)

if response is None:
    print("CACHE MISS")

    response = "Python est un langage de programmation."

    set_cached_response(
        question,
        response,
        expiration=3600
    )
else:
    print("CACHE HIT")

print("Réponse :", response)

# Deuxième consultation
response = get_cached_response(question)

if response is not None:
    print("CACHE HIT")
    print("Réponse :", response)
