class BlaBlaException(Exception):
    pass


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


@coroutine
def subgen():
    x = 'READY'
    message = yield x
    print('Received: ', message)


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('DONE.')
            break
        except BlaBlaException:
            print('.  .  .  .  .  .  .  .  .  .  .  .  .  .  .')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average
