import timeit


class NoSlots:
    def __init__(self):
        self.a = 1
        self.b = 2


class WithSlots(object):
    __slots__ = ['a', 'b']

    def __init__(self):
        self.a = 1
        self.b = 2


class Car():
    __slots__ = ('model', 'color')

    def __init__(self, model, color):
        self.model = model
        self.color = color


if __name__ == "__main__":
    timeit.repeat()

    ns = NoSlots()
    print(ns.__dict__)

    ws = WithSlots()
    print(ws.__slots__)

    mers = Car('Benz', 'Argentum')
    print(mers.__slots__)
    print(mers)
    print(mers.model)
    print(mers.color)

    mers.model = 'S'
    print(mers.model)

    # AttributeError Error!
    # ws = WithSlots()
    # print(ws.__dict__)