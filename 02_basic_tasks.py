import asyncio


async def send_one():
    return 1


async def greeting(timeout: int):
    await asyncio.sleep(timeout)
    return 'Hello world!'


async def main():
    res1 = asyncio.create_task(send_one())
    res2 = asyncio.create_task(greeting(2))
    res3 = asyncio.create_task(greeting(3))
    res4 = asyncio.create_task(greeting(15))
    res5 = asyncio.create_task(greeting(3))
    res6 = asyncio.create_task(greeting(2))
    
    print(await res1)
    print(await res2)
    print(await res3)
    print(await res4)
    print(await res5)
    print(await res6)


if __name__ == '__main__':
    asyncio.run(main())
    