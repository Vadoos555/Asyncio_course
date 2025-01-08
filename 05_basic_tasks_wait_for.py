import asyncio


async def greeting(timeout: int):
    await asyncio.sleep(timeout)
    return 'Hello world!'


async def main():
    long_task = asyncio.create_task(greeting(5))
    
    try:
        result = await asyncio.wait_for(
            asyncio.shield(long_task),
            timeout=2
        )
    except asyncio.TimeoutError:
        print('the long task cancelled')
        result = await long_task
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
    