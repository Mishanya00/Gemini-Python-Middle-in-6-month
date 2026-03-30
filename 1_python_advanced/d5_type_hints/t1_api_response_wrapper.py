import uuid
from typing import Generic, TypeVar
import time


T = TypeVar('T')


class ApiResponse(Generic[T]):
    def __init__(self, data: T, status: str):
        self.data = data
        self.status = status
        self.timestamp = time.time()


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Transaction:
    def __init__(self, amount: str, receiver_uuid: uuid.UUID, sender_uuid: uuid.UUID):
        self.receiver_uuid = receiver_uuid
        self.sender_uuid = sender_uuid
        self.amount = amount


user = User('Alex', 12)
t1 = Transaction('100', uuid.uuid4(), uuid.uuid4())
t2 = Transaction('200', uuid.uuid4(), uuid.uuid4())
t3 = Transaction('300', uuid.uuid4(), uuid.uuid4())


a = ApiResponse[User](
    user,
    'success'
)

b = ApiResponse[User](
    t1,
    'success'
)

c = ApiResponse[Transaction](
    t2,
    'fail'
)

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)