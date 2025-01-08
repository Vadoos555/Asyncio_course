import asyncio


async def coro_norm():
    return 'Hello world'


async def coro_value_error():
    raise ValueError


async def coro_long():
    try:
        print('Long task is running...')
        await asyncio.sleep(2)
        print('Long task completed')
        return 'Long task'
    
    except asyncio.CancelledError as err:
        print('All needed actions are done')
        raise asyncio.CancelledError


async def main():
    
   try:
        async with asyncio.TaskGroup() as tg:
        
            res1 = tg.create_task(coro_norm())
            res2 = tg.create_task(coro_value_error())
            res3 = tg.create_task(coro_long())
        
        results = [res1.result(), res2.result(), res3.result()]
        print(results)
    
   except* ValueError as err:
       print(f'{err=}')


if __name__ == '__main__':
    asyncio.run(main())
    