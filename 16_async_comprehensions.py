import asyncio

from faker import Faker


faker = Faker('en_US')


async def get_users(n=1):
    await asyncio.sleep(0.2)
    
    for i in range(n):
        name, surname = faker.name_male().split()
        yield name, surname


async def main():
    lst = [name async for name in get_users(3)]
    
    dct = {name: surname async for name, surname in get_users(5)}
    
    st = {name async for name in get_users(4)}
    
    print(lst)
    print(dct)
    print(st)


if __name__ == '__main__':
    asyncio.run(main())
    