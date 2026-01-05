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


if __name__ == "__main__":
    timeit.repeat()

    ns = NoSlots()
    print(ns.__dict__)

    ws = WithSlots()
    print(ws.__slots__)

    # AttributeError Error!
    # ws = WithSlots()
    # print(ws.__dict__)