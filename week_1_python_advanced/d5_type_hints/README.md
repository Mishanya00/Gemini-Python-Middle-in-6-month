### Day 5: Advanced Type Hinting & Pydantic V2
*Why? Fintech requires strict contracts. "Maybe it's a string" is not acceptable.*

**Topics:**
*   `typing` module: `Optional`, `Union`, `Any`, `Callable`.
*   **Generics:** `TypeVar`, `Generic[T]`.
*   `typing.Protocol` (Structural subtyping / Duck typing interface).
*   Pydantic V2: Validators (`@field_validator`), Computed fields.

**Practical Tasks:**
1.  **Generic Response Wrapper:** Create a generic class `ApiResponse[T]` (where T is data). It should have `status: str`, `data: T`, and `timestamp`. Instantiate it with `User` model and `Transaction` model.
2.  **Strict Pydantic Validation:** Create a `TransferRequest` model.
    *   Fields: `sender_id`, `receiver_id`, `amount`, `currency`.
    *   Validator: `sender_id` must not equal `receiver_id`.
    *   Validator: `amount` must be positive.
    *   Computed Field: `commission` (automatically calculated as 1% of amount).