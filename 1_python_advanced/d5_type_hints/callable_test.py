from collections.abc import Callable, Awaitable


def summ(a: int, b: int) -> float:
    return a + b + 0.01


async def async_summ(a: int, b: int) -> float:
    return a + b + 0.01 + 0.093


def concat(str1: str, str2: str, str3: str) -> str:
    return str1 + str2 + str3

callback: Callable[[int, int], float] = summ
callback2: Callable[[int, int], Awaitable[float]] = async_summ

# callback3: Callable[[...], str] = concat
callback4: Callable[..., str] = concat