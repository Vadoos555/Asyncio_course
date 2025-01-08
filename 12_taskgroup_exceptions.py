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
        async with asyncio.TaskGroup() as tg:
        
            res1 = tg.create_task(coro_norm())
            res2 = tg.create_task(coro_value_error())
            res3 = tg.create_task(coro_type_error())
        
        results = [res1.result(), res2.result(), res3.result()]
    
   except* ValueError as err:
       print(f'{err=}')
   except* TypeError as err:
       print(f'{err=}')
   else:
       print(f'{results=}')


if __name__ == '__main__':
    asyncio.run(main())
    