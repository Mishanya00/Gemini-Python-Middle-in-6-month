from typing_extensions import Self
from decimal import Decimal, ROUND_HALF_UP
from functools import cached_property

from pydantic import (
    BaseModel,
    model_validator,
    field_validator,
    computed_field, ValidationError,
)


class TransferRequest(BaseModel):
    sender_id: int
    receiver_id: int
    amount: Decimal
    currency: str

    @model_validator(mode='after')
    def check_self_transfer(self) -> Self:
        if self.sender_id == self.receiver_id:
            raise ValueError('Self transfer is not allowed')
        return self

    @field_validator('amount')
    @classmethod
    def check_positive(cls, v: Decimal) -> Decimal:
        if v <= Decimal('0.00'):
            raise ValueError('Amount must be positive')
        return v

    @computed_field
    @cached_property
    def commission(self) -> Decimal:
        return Decimal('0.01') * self.amount


def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}')")


print_separator('HAPPY PATH')

try:
    t1 = TransferRequest(
        sender_id=100,
        receiver_id=200,
        amount=Decimal('500.00'),
        currency='USD'
    )

    print(f'Transaction Created: {t1}')
    print(f'   Amount: {t1.amount} (Type: {type(t1.amount).__name__})')

    print(f'   Commission (1%): {t1.commission}')

    # Serialization (JSON)
    # Notice 'commission' is included automatically due to @computed_field
    print(f'   JSON Output: {t1.model_dump_json()}')

except ValidationError as e:
    print(e)


print_separator('ERROR: SELF TRANSFER')

try:
    TransferRequest(
        sender_id=100,
        receiver_id=100,  # SAME ID
        amount=Decimal('50.00'),
        currency='EUR'
    )
except ValidationError as e:
    print('Validation Caught:')
    for err in e.errors():
        print(f'   - Location: {err['loc']}')
        print(f'     Msg: {err['msg']}')
        print(f'     Type: {err['type']}')

print_separator('ERROR: NEGATIVE AMOUNT')

try:
    TransferRequest(
        sender_id=100,
        receiver_id=200,
        amount=-Decimal('150.00'), # negative
        currency='USD'
    )
except ValidationError as e:
    print('Validation Caught:')
    for err in e.errors():
        print(f'   - Field: {err['loc']}')
        print(f'     Msg: {err['msg']}')

print_separator('ERROR: INVALID TYPE')

try:
    TransferRequest(
        sender_id=100,
        receiver_id=200,
        amount='not-a-number',
        currency='USD'
    )
except ValidationError as e:
    print('Validation Caught:')
    print(f'   Msg: {e.errors()[0]['msg']}')
