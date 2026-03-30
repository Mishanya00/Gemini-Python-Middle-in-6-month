import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Creates a reference cycle

a = Node(10)
b = Node(20)

a.next = b
b.next = a # (circular reference)

del a, b  # Deleting references, but the objects remain in memory

gc.collect()  # Python's garbage collector removes them