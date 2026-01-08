import functools
import time


def timeit():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            print(f'Function {func.__name__} execution time:',  end - start)

            return result
        return wrapper
    return decorator


@timeit()
def cycle_n(n: int):
    a = 0
    for _ in range(n):
        a += 1
    return a


print(cycle_n(1))
print(cycle_n(10))
print(cycle_n(100))
print(cycle_n(1000))
print(cycle_n(10000))
print(cycle_n(100000))
print(cycle_n(1000000))
print(cycle_n(10000000))