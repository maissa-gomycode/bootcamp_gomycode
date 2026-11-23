
import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


def get_cached_response(key: str):
    value = redis_client.get(key)

    if value is None:
        return None

    return json.loads(value)


def set_cached_response(
    key: str,
    response: str,
    expiration: int = 3600
):
    redis_client.setex(
        key,
        expiration,
        json.dumps(response)
    )


def clear_cache():
    redis_client.flushdb()
