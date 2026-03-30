import aiohttp
import asyncio


BASE_URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_post(post_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BASE_URL}/{post_id}') as resp:
            return await resp.json()


async def main():
    post_id = int(input('Enter post id: '))
    data = await fetch_post(post_id)
    print(data.get('title', None))


asyncio.run(main())