import asyncio
import aiohttp


class AsyncSession:
    def __init__(self, url):
        self.url = url
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self.url)
        return response
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()  


async def check(url):
    async with AsyncSession(url) as response:
        html = await response.text()
        return f'{url}: {html[:20]}'


async def main():
    async with asyncio.TaskGroup() as tg:
        print(type(tg))
        print(dir(tg))
        print()
    
        res1 = tg.create_task(check('https://facebook.com'))
        res2 = tg.create_task(check('https://youtube.com'))
        res3 = tg.create_task(check('https://google.com'))
    
    print(res1.result())
    print(res2.result())
    print(res3.result())


if __name__ == '__main__':
    asyncio.run(main())
    