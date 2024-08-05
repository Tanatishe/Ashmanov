import aiohttp


async def redirect(request):

    user_agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    url = "https://www.google.com/"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=f"{url}search?q={request}", headers=user_agent
        ) as response:
            html = await response.text()
            return html
