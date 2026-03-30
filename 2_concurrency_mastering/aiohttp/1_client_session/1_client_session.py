import aiohttp
import asyncio
import orjson


BASE_URL = 'http://httpbin.org'


async def get_post_put():
    async with aiohttp.ClientSession(BASE_URL) as session:
        async with session.get('/get') as resp:
            print('--- GET ---')
            print(resp.status)
            print(await resp.text())
        async with session.post('/post', data=b'data') as resp:
            print('--- POST ---')
            print(resp.status)
            print(await resp.text())
        async with session.put('/put', data=b'data') as resp:
            print('--- PUT ---')
            print(resp.status)
            print(await resp.text())


async def parametrized_get(**kwargs):
    async with aiohttp.ClientSession(BASE_URL) as session:
        async with session.get('/get', params=kwargs) as resp:
            print('--- GET ---')
            print(resp.status)
            print(await resp.text())


async def post_with_orjson(**kwargs):
    async with aiohttp.ClientSession(BASE_URL, json_serialize=orjson.dumps) as session:
        async with session.post(BASE_URL + '/post', data=kwargs) as resp:
            print('post_with_orjson():')
            print(resp.status)
            print(await resp.text())



async def main():
    print('Aiohttp example client started.')
    # await get_post_put
    # await parametrized_get(key1='value1', money=9.90)

    await post_with_orjson(key='value')

    print('Aiohttp example client finished.')


asyncio.run(main())
