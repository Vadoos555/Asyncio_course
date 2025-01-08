import asyncio
from random import randint


class C:
    norm = '\033[0m'
    blue = '\033[94m'
    green = '\033[92m'


async def producer(queue, name):
    timeout = randint(1, 5)
    await queue.put(timeout)
    print(f'{C().blue}Producer {name} put {timeout} to the queue {queue}{C().norm}')


async def consumer(queue, name):
    while True:
        timeout = await queue.get()
        await asyncio.sleep(timeout)
        print(f'{C().green}Consumer {name} ate {timeout}, {queue}{C().norm}')
        queue.task_done()
    

async def main():
    queue = asyncio.Queue(maxsize=3)
    
    producers = [producer(queue, name=i) for i in range(12)]
    consumers = [asyncio.create_task(consumer(queue, name=i)) for i in range(4)]
    
    await asyncio.gather(*producers)
    await queue.join()
    
    for c in consumers:
        c.cancel()
    

if __name__ == '__main__':
    asyncio.run(main())
    