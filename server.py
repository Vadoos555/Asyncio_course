import asyncio
import uvicorn

from fastapi import FastAPI


app = FastAPI()

lock = asyncio.Lock()
count = 0


@app.get('/')
async def main():
    global count
    
    async with lock:
        count += 1
    
    return {'count': count}


@app.get('/hello')
async def greet():
    return {'message': 'Hello World.'}


if __name__ == '__main__':
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
    