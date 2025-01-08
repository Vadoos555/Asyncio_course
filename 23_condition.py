import asyncio
from random import randint


async def waiter(condition: asyncio.Condition, id: int):
    async with condition:
        print(f'Waiter {id+1} is awaiting')
        await condition.wait()
        
        num = randint(1, 5)
        print(f'Waiter {id+1} generated {num}')


async def starter(condition: asyncio.Condition):
    print('Starter is sleeping for 3 sec.')
    await asyncio.sleep(3)
    
    async with condition:
        condition.notify_all()


async def main():
  condition = asyncio.Condition()
  
  waiters = [
      asyncio.create_task(waiter(condition, id=i))
      for i in range(5)
  ]
  asyncio.create_task(starter(condition))
  
  await asyncio.gather(*waiters)


if __name__ == '__main__':
    asyncio.run(main())
    