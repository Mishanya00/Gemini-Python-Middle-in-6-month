import os
import uuid


class JuniorIsNotNeededError(Exception):
    pass


class SafeWriter:
    def __init__(self, filename):
        self.temp_filename = str(uuid.uuid4()) + '.txt'
        self.filename = filename

    def __enter__(self):
        self.f = open(self.temp_filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        if exc_type is not None:
            os.remove(self.temp_filename)
        else:
            os.remove(self.filename)
            os.rename(self.temp_filename, self.filename)
        return True

    def write(self, text):
        self.f.write(text)


writer = SafeWriter('test.txt')
with writer as f:
    f.write('Middle, guys!')

with writer as f:
    f.write('Senior, guys!')

with writer as f:
    f.write('Junior, guys!')
    raise JuniorIsNotNeededError