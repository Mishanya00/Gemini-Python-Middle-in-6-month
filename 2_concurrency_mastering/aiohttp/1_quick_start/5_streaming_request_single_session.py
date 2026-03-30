import time
import functools
import asyncio
import aiohttp


BASE_URL_4 = "https://science.nasa.gov/wp-content/uploads/2023/06/webb-flickr-52259221868-30e1c78f0c-4k-jpg.webp"
FILENAME_STREAM = 'nasa_stream.png'
FILENAME_FETCH = 'nasa_fetch.png'


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

            avg_dt_ms = total_ms / rounds
            print(f'Results for `{func.__name__}`:')
            print(f'  Average: {avg_dt_ms:.2f} ms')
            print(f'  Total:   {total_ms:.2f} ms for {rounds} rounds\n')
        return wrapper
    return decorator


async def streaming_fetch(session: aiohttp.ClientSession, base_url: str, filename: str):
    async with session.get(base_url) as resp:
        if resp.status != 200:
            raise RuntimeError(f'Status code: {resp.status}')

        with open(filename, 'wb') as f:
            async for chunk in resp.content.iter_chunked(1024):
                f.write(chunk)

async def fetch(session: aiohttp.ClientSession, base_url: str, filename: str):
    async with session.get(base_url) as resp:
        if resp.status != 200:
            raise RuntimeError(f'Status code: {resp.status}')

        content = await resp.read()
        with open(filename, 'wb') as f:
            f.write(content)


@async_timedelta(rounds=100)
async def streaming_fetch_benchmark(session: aiohttp.ClientSession, base_url: str, filename: str):
    await streaming_fetch(session, base_url, filename)


@async_timedelta(rounds=100)
async def fetch_benchmark(session: aiohttp.ClientSession, base_url: str, filename: str):
    await fetch(session, base_url, filename)


async def main():
    async with aiohttp.ClientSession() as session:
        await streaming_fetch_benchmark(session, base_url=BASE_URL_4, filename=FILENAME_STREAM)
        await fetch_benchmark(session, base_url=BASE_URL_4, filename=FILENAME_FETCH)


if __name__ == '__main__':
    asyncio.run(main())
