from itertools import islice, chain, cycle


def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1


def gen_list():
    a = [1,2,3,4,5]
    yield from a


a = gen_list
b = gen_list()
print(a)
print(b)
for el in b:
    print(el, end=' ')

a = infinite_seq()
for i in range(10):
    print(next(a), end=' ')

print()

a = infinite_seq()
for el in islice(a, 10, 20):
    print(el, end=' ')

print()

a = infinite_seq()
first_10 = [next(a) for _ in range(10)]
print(first_10)


