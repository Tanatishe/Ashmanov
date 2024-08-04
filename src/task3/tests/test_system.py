import asyncio
import aiohttp



def test_request(req:str):
    r = requests.get(f"http://127.0.0.1:8000?q={req}")
    print(r.text)


async def main():
    for i in range(10):
        task = asyncio.create_task(test_request(str(i)))
        await task

asyncio.run(main())