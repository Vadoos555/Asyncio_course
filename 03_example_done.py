import asyncio


async def coro():
    return 555


async def main():
    task = asyncio.create_task(coro())
    
    await task
    print(task.done())
    print(task.cancelled())


if __name__ == '__main__':
    asyncio.run(main())
    