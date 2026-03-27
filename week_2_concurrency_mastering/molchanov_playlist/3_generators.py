from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

        sum = 234 + 234
        print(sum)


# g = gen_filename()


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('michael')
g2 = gen2(4)

tasks = [g1, g2]


# Round Robin - Карусель задач
while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i) # Some task here
        tasks.append(task)
    except StopIteration:
        pass
