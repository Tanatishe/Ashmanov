import aiohttp
import asyncio


async def main(req):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://127.0.0.1:8000?q={req}") as response:
            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])
            html = await response.text()
            print(type(html))
            print("Body:", html[:15], "...")


for i in "kljklпар":
    asyncio.run(main(i))
