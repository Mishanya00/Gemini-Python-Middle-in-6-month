import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # should be 2 due to function argument

y = x
print(sys.getrefcount(x))

del x
print(sys.getrefcount(y))

del y