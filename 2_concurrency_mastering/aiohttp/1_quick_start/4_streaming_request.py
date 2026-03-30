import time
import functools
import asyncio

import aiohttp


BASE_URL_1 = 'https://jsonplaceholder.typicode.com/posts'
FILENAME_1 = 'posts.json'

BASE_URL_2 = 'https://api.github.com/events'
FILENAME_2 = 'github_events.json'

BASE_URL_3 = "https://httpbin.org/image/png"
FILENAME_3 = 'pastebin.png'

BASE_URL_4 = "https://science.nasa.gov/wp-content/uploads/2023/06/webb-flickr-52259221868-30e1c78f0c-4k-jpg.webp"
FILENAME_4 = 'nasa.png'


def async_timedelta(rounds=10):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            print(f'--- Benchmark: {func.__name__} starting ({rounds} rounds) ---')
            total_ms = 0

            for i in range(rounds):
                start_time = time.perf_counter()

                await func(*args, **kwargs)

                finish_time = time.perf_counter()
                dt_ms = (finish_time - start_time) * 1000
                total_ms += dt_ms
                # print(f"  Round {i + 1}: {dt_ms:.2f} ms")

            avg_dt_ms = total_ms / rounds
            print(f'Results for `{func.__name__}`:')
            print(f'  Average: {avg_dt_ms:.2f} ms')
            print(f'  Total:   {total_ms:.2f} ms for {rounds} rounds\n')

        return wrapper

    return decorator


async def streaming_fetch(base_url: str, filename: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{base_url}') as resp:
            if resp.status != 200:
                raise RuntimeError(f'Status code: {resp.status}')

            with open (filename, 'wb') as f:
                async for chunk in resp.content.iter_chunked(1024):
                    f.write(chunk)


async def fetch(base_url: str, filename: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{base_url}') as resp:
            if resp.status != 200:
                raise RuntimeError(f'Status code: {resp.status}')

            with open (filename, 'wb') as f:
                f.write(await resp.read())


@async_timedelta(rounds=25)
async def streaming_fetch_benchmark(base_url: str, filename: str):
    await streaming_fetch(BASE_URL_4, FILENAME_4)


@async_timedelta(rounds=25)
async def fetch_benchmark(base_url: str, filename: str):
    await fetch(BASE_URL_4, FILENAME_4)


async def main():
    await streaming_fetch_benchmark(base_url=BASE_URL_4, filename=FILENAME_4)
    await fetch_benchmark(base_url=BASE_URL_4, filename=FILENAME_4)


asyncio.run(main())
