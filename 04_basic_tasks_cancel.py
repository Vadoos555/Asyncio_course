import asyncio


async def greeting(timeout: int):
    await asyncio.sleep(timeout)
    return 'Hello world!'


async def main():
    long_task = asyncio.create_task(greeting(60))
    
    seconds = 0
    
    while not long_task.done():
        await asyncio.sleep(1)
        seconds += 1
        
        if seconds == 5:
            long_task.cancel()
            
        print('time passed: ', seconds)
    
    try:
        await long_task
    except asyncio.CancelledError:
        print('the long task cancelled')


if __name__ == '__main__':
    asyncio.run(main())
    