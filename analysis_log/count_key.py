import redis

REDIS_HOST = "host"
REDIS_PORT = "port"
REDIS_USER = "user"
REDIS_PASSWORD = "password"
KEY_PATTERN = "key*"

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, username=REDIS_USER, password=REDIS_PASSWORD)

def count_keys(pattern):
    cursor = 0
    count = 0
    while True:
        cursor, keys = r.scan(cursor=cursor, match=pattern, count=1000)
        count += len(keys)
        if cursor == 0:
            break
    return count

total_keys = count_keys(KEY_PATTERN)
print(f"Total keys matching '{KEY_PATTERN}': {total_keys}")
