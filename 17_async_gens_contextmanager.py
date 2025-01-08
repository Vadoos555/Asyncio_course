import asyncio

from contextlib import contextmanager, asynccontextmanager
from redis import asyncio as aioredis


@contextmanager
def custom_open(filename: str, mode='w'):
    file_object = open(filename, mode)
    yield file_object
    file_object.close()
    

# with custom_open('file.txt') as file:
#     file.write('Hello world.')


@asynccontextmanager
async def redis_connection():
    try:
        redis = await aioredis.from_url('redis://localhost')
        yield redis
    finally:
        await redis.close()


async def main():
    async with redis_connection() as redis:
        await redis.set('kovalenko', 'stepan')
        await redis.set('ivanenko', 'ivan')
        await redis.set('petrenko', 'petro')
        await redis.set('vader', 'darth')
    

if __name__ == '__main__':
    asyncio.run(main())
    