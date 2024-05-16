import redis


def redis_get(key):
    with redis.Redis(host='127.0.0.1', port=6379) as redis_client:
        num = redis_client.get(key)

    return num


def redis_set(key, value):
    with redis.Redis(host='127.0.0.1', port=6379) as redis_client:
        redis_client.set(key, value)