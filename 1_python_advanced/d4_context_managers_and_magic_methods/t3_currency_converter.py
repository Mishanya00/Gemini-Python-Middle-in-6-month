import re
from typing import Any
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


class CurrencyConverter:
    _KEY_PATTERN = re.compile(r'^[A-Za-z]{3}$')

    def __init__(self, rates: dict):
        self._validate_dict_structure(rates)
        self.rates = self._convert_and_store(rates)

    def __call__(self, amount: Any, from_currency: str):
        try:
            amount_decimal = Decimal(str(amount))
        except Exception as e:
            raise ValueError(f"Invalid amount: {amount} ({e})")

        rate = self.rates[from_currency.upper()]

        converted = amount_decimal * rate

        rounded = converted.quantize(
            Decimal('1.00'),
            rounding=ROUND_HALF_UP
        )

        return rounded

    @classmethod
    def _validate_dict_structure(cls, data: dict[str, Any]) -> None:
        if not data:
            raise ValueError('Exchange rates cannot be empty')

        errors = []

        for key, value in data.items():
            if not cls._KEY_PATTERN.match(key):
                errors.append(f"Key {key} is not a string (type: {type(key).__name__})")
            elif not cls._KEY_PATTERN.match(key):
                errors.append(f"Key '{key}' must be exactly 3 letters")

            try:
                # Try conversion but don't store yet
                _ = Decimal(str(value))
            except (InvalidOperation, ValueError, TypeError) as e:
                errors.append(f"Value for key '{key}' cannot be converted to Decimal: {e}")

            if errors:
                error_msg = "Dictionary validation failed:\n" + "\n".join(f"  - {err}" for err in errors)
                raise ValueError(error_msg)

    @staticmethod
    def _convert_and_store(data: dict[str, Any]):
        return {
            key.upper(): Decimal(str(value))  # Normalize keys to uppercase
            for key, value in data.items()
        }


rates = {
    'usd': 2,
    'EUR': 3,
    'CHN': 0.11,
    'toR': 94.3,
}

converter = CurrencyConverter(rates)
print(converter.rates)

print(converter(115, 'USD'))
print(converter(115, 'EUR'))
print(converter(1, 'toR'))
