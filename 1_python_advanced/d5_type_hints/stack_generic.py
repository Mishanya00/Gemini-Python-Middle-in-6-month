from typing import Generic, TypeVar


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return not self.items


st = Stack[int]()
st.push(1)
st.push(2)
st.push(3)

print(st.pop())
print(st.is_empty())
print(st.pop())
print(st.is_empty())
print(st.pop())
print(st.is_empty())


class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

Box(1)
Box[int](1)
Box[int]('some string')