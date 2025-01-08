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
    
    task1 = asyncio.create_task(coro_norm())
    task2 = asyncio.create_task(coro_value_error())
    task3 = asyncio.create_task(coro_long(), name='Coro Long')
    
    tasks = [task1, task2, task3]
    
    try:
        results = await asyncio.gather(*tasks)
    
    except ValueError as err:
        print(f'{err=}')
    else:
        print(f'{results=}')
    
    for task in tasks:
        if task.done() is False:
            task.cancel()
            print(f'Pending: {task.get_name()}')
   
    print()
    
    await asyncio.sleep(2)
    print(f'{task1._state}')
    print(f'{task2._state}')
    print(f'{task3._state}')
   

if __name__ == '__main__':
    asyncio.run(main())
    