import asyncio


async def coro():
    return 555


async def main():
    task = asyncio.create_task(coro())
    
    print(dir(task))


if __name__ == '__main__':
    asyncio.run(main())
    