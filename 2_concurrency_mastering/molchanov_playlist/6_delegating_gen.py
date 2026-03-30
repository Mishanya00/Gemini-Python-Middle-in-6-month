class BlaBlaException(Exception):
    pass


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


# Should be disabled when `yield from` is used
# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except BlaBlaException:
            print('Bla-Bla; Ku-ku!!!')
        except StopIteration:
            break
        else:
            print('[SUBGEN] Received:', message)

    return 'finished execution for subgen()'


@coroutine
def delegator(subgen):
    while True:
        try:
            data = yield
            subgen.send(data)
        except BlaBlaException as e:
            subgen.throw(e)


@coroutine
def delegator_simplified(subgen):
    result = yield from subgen
    print(result)


def test_gen_yield_from():
    yield from 'misha'
