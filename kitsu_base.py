import requests
import asyncio
import aiohttp

BASE_API_PATH = 'https://kitsu.io/api/edge'

url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
params = {'language': "ru"}

r = requests.get(url=url, params=params)

print(r.json())

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            r = await response.read()
            print(r)

asyncio.get_event_loop().run_until_complete(main())