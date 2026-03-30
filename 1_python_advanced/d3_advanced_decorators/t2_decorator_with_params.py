import functools
import time
from random import randint


class ProbabilityError(Exception):
    pass


class MaxRetriesExceededError(Exception):
    pass


def probability_function():
    a = randint(0, 100)
    if a < 80:
        raise ProbabilityError
    print('Success!')


def retry(max_retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except ProbabilityError:
                    print('Connection error')
                    time.sleep(delay)
            raise MaxRetriesExceededError
        return wrapper
    return decorator


@retry(max_retries=5, delay=2)
def call_probability_function():
    probability_function()


call_probability_function()