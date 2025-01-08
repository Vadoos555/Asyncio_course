import asyncio


async def send_one():
    return 1


async def greeting():
    await asyncio.sleep(2)
    return 'Hello world!'


async def main():
    res1 = await send_one()
    res2 = await greeting()
    
    print(res1)
    print(res2)


if __name__ == '__main__':
    asyncio.run(main())
    