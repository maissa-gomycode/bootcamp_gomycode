import redis
from functools import lru_cache
import time

cache = {}

# Connexion au serveur Redis
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


# Enregistrer une donnée dans le cache
def set_cache(key, value):
    redis_client.set(key, value, ex=300)


# Récupérer une donnée du cache
def get_cache(key):
    return redis_client.get(key)


# Supprimer une donnée du cache
def delete_cache(key):
    redis_client.delete(key)


@lru_cache(maxsize=100)
def get_cached_response(question: str):
    return None


def get_cached_response(key: str):
    item = cache.get(key)

    if item is None:
        return None

    response, expiration_time = item

    if time.time() > expiration_time:
        del cache[key]
        return None