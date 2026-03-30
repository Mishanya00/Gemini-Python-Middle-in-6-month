from time import sleep
from itertools import cycle


def read_file_line(filename):
    with open(filename) as f:
        for line in f:
            yield line


def filter_critical_message(filename):
    line_reader = (read_file_line(filename))
    for line in line_reader:
        if line.split()[2] == '[CRITICAL]':
            yield line


line_reader = read_file_line('advanced.log')
critical_reader = filter_critical_message('advanced.log')

counter = 0
for el in critical_reader:
    print(el.strip())
    counter += 1

print(f'Total critical logs count: {counter}')


# little experiment
# line_reader = read_file_line('test.txt')
#
# for el in cycle(line_reader):
#     print(el)
#     sleep(1)
