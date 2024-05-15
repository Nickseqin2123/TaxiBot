import redis


def redis_get(user_id):
    with redis.Redis(host='127.0.0.1', port=6379) as redis_client:
        num = redis_client.get(user_id)

    return num


def redis_set(user_id, telephone_number):
    with redis.Redis(host='127.0.0.1', port=6379) as redis_client:
        redis_client.set(user_id, telephone_number)