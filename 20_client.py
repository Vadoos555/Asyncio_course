import asyncio
import time

import aiohttp


lock = asyncio.Lock()


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with lock:
            async with session.get(url) as response:
                data = await response.json()
                print(data)


async def without_lock(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data)


async def get_data(url):
    await make_request(url)


async def main():
    start = time.monotonic()
    
    tasks = [
        asyncio.create_task(get_data('http://localhost:8000'))
        for _ in range(20)
    ]
    
    tasks_no_locks = [
        asyncio.create_task(without_lock('http://localhost:8000/hello'))
        for _ in range(5)
    ]
    
    await asyncio.gather(*tasks, *tasks_no_locks)
    
    print(time.monotonic() - start)


if __name__ == '__main__':
    asyncio.run(main())
    