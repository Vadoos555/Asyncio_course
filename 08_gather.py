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
        print(f'{url}: {html[:20]}')
        

class ServerError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message
    

async def get_server_error():
    await asyncio.sleep(2)
    raise ServerError('Failed to get data')


async def main():
    ulrs = [
        'https://facebook.com',
        'https://youtube.com',
        'https://google.com'
    ]
    
    group1 = asyncio.gather(
        check('https://facebook.com'),
        check('https://youtube.com')
    )

    group2 = asyncio.gather(
        check('https://google.com'),
        check('https://youtube.com')
    )
    
    groups = asyncio.gather(group1, group2)
    
    results = await groups
    
    # coros = [check(url) for url in ulrs]
    
    # for coro in asyncio.as_completed(coros):
    #     result = await coro
    #     print(result)
    
    # results = asyncio.gather(
    #     *coros, 
    #     get_server_error(),
    #     return_exceptions=True
    #     )    
    
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
    