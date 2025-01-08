import asyncio

import aiohttp


async def make_request(url, condition):
    async with aiohttp.ClientSession() as session:
        async with condition:
            await condition.wait()
            async with session.get(url) as response:
                data = await response.json()
                print(data)


async def without_lock(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data)


async def get_data(url, condition):
    await make_request(url, condition)


async def starter(condition: asyncio.Condition):
    print('Will start after 3 seconds')
    await asyncio.sleep(3)
    async with condition:
        condition.notify_all()


async def main():
    condition = asyncio.Condition()
    
    tasks = [
        asyncio.create_task(get_data('http://localhost:8000', condition))
        for _ in range(20)
    ]
    
    tasks_no_locks = [
        asyncio.create_task(without_lock('http://localhost:8000/hello'))
        for _ in range(5)
    ]
    
    asyncio.create_task(starter(condition))
    
    await asyncio.gather(*tasks, *tasks_no_locks)


if __name__ == '__main__':
    asyncio.run(main())
    