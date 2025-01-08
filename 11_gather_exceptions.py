import asyncio
import aiohttp


async def coro_norm():
    return 'Hello world'


async def coro_value_error():
    raise ValueError


async def coro_type_error():
    raise TypeError


async def main():
    try:
        results = await asyncio.gather(
            coro_norm(),
            coro_value_error(),
            coro_type_error(),
            return_exceptions=True
        )
        
        print(f'{results=}')
    except ValueError as err:
        print(f'{err=}')
    except TypeError as err:
        print(f'{err=}')
    
    # async with asyncio.TaskGroup() as tg:
    
    #     res1 = tg.create_task(check('https://facebook.com'))
    #     res2 = tg.create_task(check('https://youtube.com'))
    #     res3 = tg.create_task(check('https://google.com'))
    
    # print(res1.result())
    # print(res2.result())
    # print(res3.result())


if __name__ == '__main__':
    asyncio.run(main())
    