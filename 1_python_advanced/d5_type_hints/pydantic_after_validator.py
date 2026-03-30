from typing import Annotated

from pydantic import AfterValidator, BaseModel


def is_even(value: int) -> int:
    if value % 2 == 1:
        raise ValueError(f'{value} is not an even number')
    return value


EvenNumber = Annotated[int, AfterValidator(is_even)]


class Model1(BaseModel):
    num: EvenNumber


class Model2(BaseModel):
    num: Annotated[EvenNumber, AfterValidator(lambda v: v + 2)]


class Model3(BaseModel):
    num_list: list[EvenNumber]


print('----------------------------------------------------------------------')
try:
    a = Model1(num=1)
except ValueError as e:
    print(e)
print('----------------------------------------------------------------------')

try:
    a = Model1(num=2)
    print(f'Successfully validated {a.__class__} with value {a.num}')
except ValueError as e:
    print(e)
print('----------------------------------------------------------------------')

try:
    a = Model2(num=3)
    print(f'Successfully validated {a.__class__} with value {a.num}')
except ValueError as e:
    print(e)
print('----------------------------------------------------------------------')

try:
    a = Model2(num=4)
    print(f'Successfully validated {a.__class__} with value {a.num}')
except ValueError as e:
    print(e)
print('----------------------------------------------------------------------')

try:
    a = Model3(num_list=5)
    print(f'Successfully validated {a.__class__} with value {a.num_list}')
except ValueError as e:
    print(e)
print('----------------------------------------------------------------------')

try:
    a = Model3(num_list=[2, 4, 6, 1])
    print(f'Successfully validated {a.__class__} with value {a.num_list}')
except ValueError as e:
    print(e)
print('----------------------------------------------------------------------')

try:
    a = Model3(num_list=[2, 4, 6])
    print(f'Successfully validated {a.__class__} with value {a.num_list}')
except ValueError as e:
    print(e)
print('----------------------------------------------------------------------')