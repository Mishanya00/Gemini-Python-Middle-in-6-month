import types
import asyncio
from time import time


# -----------------------------------------------------------------------
# Code written in Python 3.4 style when asyncio was introduced
# -----------------------------------------------------------------------

#asyncio.coroutine - deprecated and removed
@types.coroutine # func becomes coroutine based on generator
def print_nums_python34():
    num = 0
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(1)


@types.coroutine
def print_time_python34():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds are passed')
        count += 1
        yield from asyncio.sleep(1)


@types.coroutine
def main_python34():
    task1 = asyncio.ensure_future(print_nums_python34())
    task2 = asyncio.ensure_future(print_time_python34())

    yield from asyncio.gather(task1, task2)


# Python 3.x < 3.7 style:
# if __name__ == '__main__':
#     # loop = asyncio.get_event_loop() # deprecated
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     try:
#         loop.run_until_complete(main_python34())
#     finally:
#         loop.close()


# -----------------------------------------------------------------------
# Python ~3.5-3.7+:
# -----------------------------------------------------------------------

async def print_nums():
    num = 0
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds are passed')
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums)
    task2 = asyncio.create_task(print_time)

    await asyncio.gather(task1, task2)


# Python 3.7+:
if __name__ == '__main__':
    asyncio.run(main())