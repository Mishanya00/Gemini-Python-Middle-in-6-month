from time import time

import requests


BASE_URL = 'https://loremflickr.com/320/240'


def get_file(url):
    resp = requests.get(url, allow_redirects=True)
    return resp


def write_file(response):
    # https://loremflickr.com/cache/resized/5008_5314742433_a4a7a4eb87_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    with open (filename, 'wb') as f:
        f.write(response.content)


# ~2 second
def main():
    t0 = time()

    url = BASE_URL

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


# if __name__ == '__main__':
#     main()


###################################################


import asyncio
import aiohttp


def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))

    with open(filename, 'wb') as f:
        f.write(data)


async def fetch_content(session, url):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        write_image(data)


# ~0.25 seconds
async def main2():
    url = BASE_URL
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)