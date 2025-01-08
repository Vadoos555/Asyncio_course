import asyncio


async def coro(message: str):
    print(message)
    await asyncio.sleep(1)
    print(message)


async def main():
    # print(asyncio.all_tasks())
    print('--main beginning--')
    
    asyncio.create_task(coro('***text***'))
    
    await asyncio.sleep(1)
    
    print('--main done--')


if __name__ == '__main__':
    asyncio.run(main())
    