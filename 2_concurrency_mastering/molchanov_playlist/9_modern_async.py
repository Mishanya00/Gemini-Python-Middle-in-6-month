import asyncio
import httpx
import time
from pathlib import Path


BASE_URL = 'https://loremflickr.com/320/240'
SAVE_DIR = Path("./images")
SAVE_DIR.mkdir(exist_ok=True)


def save_to_disk(content: bytes):
    filename = SAVE_DIR / f"file-{int(time.time() * 1000)}.jpeg"
    with open(filename, 'wb') as f:
        f.write(content)


async def fetch_and_save(client: httpx.AsyncClient, url: str):
    response = await client.get(url, follow_redirects=True)

    await asyncio.to_thread(save_to_disk, response.content)


async def main():
    # async with httpx.AsyncClient(http2=True) as client:
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            for _ in range(10):
                tg.create_task(fetch_and_save(client, BASE_URL))


if __name__ == '__main__':
    t0 = time.perf_counter()

    asyncio.run(main())

    print(f"Finished in: {time.perf_counter() - t0:.2f} seconds")
