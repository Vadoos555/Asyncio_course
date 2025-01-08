import asyncio
from concurrent.futures import ProcessPoolExecutor

import aiohttp
import aiofiles
from bs4 import BeautifulSoup


async def make_request(url, session):
    response = await session.get(url)
    
    if response.ok:
        return response
    else:
        print(f'{url} returned: {response.status}')


async def get_image_page(queue, session):
    url = 'https://c.xkcd.com/random/comic/'
    response = await make_request(url, session)
    await queue.put(response.url)


def _parse_link(html):
    soup = BeautifulSoup(html, 'lxml')
    image_link = 'https:' + soup.select_one('div#comic>img').get('src')
    return image_link


async def get_image_url(page_q, image_url_q, session):
    while True:
        url = await page_q.get()
        response = await make_request(url, session)
        html = await response.text()
        
        loop = asyncio.get_running_loop()
        with ProcessPoolExecutor() as pool:
            image_link = await loop.run_in_executor(pool, _parse_link, html)
        
        await image_url_q.put(image_link)
        
        page_q.task_done()


async def download_image(queue, session):
    while True:
        url = await queue.get()
        response = await make_request(url, session)
        filename = url.split('/')[-1]
        
        async with aiofiles.open(filename, 'wb') as file:
            async for chunk in response.content.iter_chunked(1024):
                await file.write(chunk)
        
        queue.task_done()


def cancel_tasks(tasks: list):
    [task.cancel() for task in tasks]


async def main():
    session = aiohttp.ClientSession()
    pages_q = asyncio.Queue()
    image_urls_q = asyncio.Queue()
    
    page_getters = [
        asyncio.create_task(get_image_page(pages_q, session)) 
        for i in range(4)
    ]
    
    url_getters = [
        asyncio.create_task(get_image_url(pages_q, image_urls_q, session))
        for i in range(4)
    ]
    
    downloaders = [
        asyncio.create_task(download_image(image_urls_q, session))
        for i in range(4)
    ]
    
    await asyncio.gather(*page_getters)
    
    await pages_q.join()
    cancel_tasks(page_getters)
    
    await image_urls_q.join()
    cancel_tasks(downloaders)
    
    await session.close()


if __name__ == '__main__':
    asyncio.run(main())
    