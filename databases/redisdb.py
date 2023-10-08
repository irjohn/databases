from redis import asyncio as aioredis
import redis
from time import time


class RedisDB:
    def __new__(self, *, asyncio=False, host="localhost", port=6379, db=0, decode_responses=True, **kwargs):
        if asyncio:
            return BaseAIORedis(host=host, port=port, db=db, decode_responses=decode_responses, **kwargs)
        else:
            return BaseRedis(host=host, port=port, db=db, decode_responses=decode_responses, **kwargs)

class BaseAIORedis(aioredis.Redis):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @classmethod
    @property
    def current_timestamp(self):
        return int(time())
    

class BaseRedis(redis.Redis):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    @classmethod
    @property
    def current_timestamp(self):
        return int(time())