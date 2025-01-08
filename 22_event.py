import asyncio
from random import randint


async def worker(event: asyncio.Event):
    print('Before calling of wait()')
    await event.wait()
    
    if event.is_set():
        print(f'Event is set, random number = {randint(1, 5)}')


async def coro(event: asyncio.Event):
    timeout = randint(3, 5)
    await asyncio.sleep(timeout)
    print(f'Event was set by coro after {timeout} sec.')
    event.set()


async def main():
    event = asyncio.Event()
    
    tasks = [asyncio.create_task(worker(event)) for _ in range(5)]
    
    asyncio.create_task(coro(event))
    
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    