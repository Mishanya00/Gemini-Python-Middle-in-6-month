# Week 1: Python Advanced Internals & Functional Patterns
**Focus:** Memory management, efficient data processing (Generators), and "Pythonic" structural patterns (Decorators/Context Managers).
**Goal:** Write code that saves RAM and uses Python's dynamic nature effectively (Meta-programming basics).

### Prerequisites
*   Python 3.10+ installed.
*   An IDE (VS Code/PyCharm) set up.
*   Repo for practice: `python-middle-road-week1`

---

### Day 1: Memory Management & Mutability
*Why? In Fintech, leaking memory in a long-running background worker is a disaster.*

**Topics:**
*   Mutable vs Immutable types (Deep dive).
*   `id()`, `is` vs `==`.
*   Pass-by-object-reference.
*   **Garbage Collection:** Reference counting vs Generational GC.
*   `__slots__`: Saving memory in classes.

**Practical Tasks:**
1.  **The "Default Arg" Trap:** Write a function with a mutable default argument (e.g., a list). Call it multiple times to demonstrate how the state persists. Fix it using `None`.
2.  **Memory Profiling:** Create a class `Transaction` with 10 fields. Create 1 million instances of it in a list. Measure RAM usage (use `sys.getsizeof` or `memory_profiler`).
3.  **Optimization:** Rewrite the class using `__slots__`. Measure RAM usage again. Calculate the % saved.

---

### Day 2: Generators & Iterators (Streaming Data)
*Why? You cannot load a 5GB CSV of transactions into RAM to process it. You must stream it.*

**Topics:**
*   Iterables vs Iterators (`__iter__`, `__next__`).
*   Generators (`yield`) and Generator Expressions.
*   `yield from` syntax.
*   `itertools` module (chain, islice, cycle).

**Practical Tasks:**
1.  **Custom Iterator:** Write a class `DateRange` that takes a start_date and end_date and iterates day by day without generating a list.
2.  **Log Parser:** Create a dummy 100MB text file (simulate logs). Write a generator function that reads the file line-by-line, filters only lines containing "ERROR", and yields the parsed timestamp and message.
3.  **Pipeline Processing:** Chain three generators:
    *   `gen_read_file`: yields lines.
    *   `gen_parse`: takes lines, yields dicts.
    *   `gen_filter`: takes dicts, yields only high-value transactions.
    *   *Run this pipeline and observe that memory usage remains flat regardless of file size.*

---

### Day 3: Advanced Decorators (Meta-programming Lite)
*Why? Used everywhere in FastAPI (Auth, Logging, Caching).*

**Topics:**
*   Closures & Scope (`nonlocal`).
*   Decorators with arguments.
*   `functools.wraps` (Why is it critical?).
*   Stacking multiple decorators.

**Practical Tasks:**
1.  **Execution Timer:** Write a `@timeit` decorator that prints how long a function took to execute.
2.  **Retry Mechanism (Critical for Fintech):** Write a `@retry(max_retries=3, delay=1)` decorator.
    *   It should catch exceptions and retry the function `max_retries` times.
    *   If it fails after all retries, raise a custom `MaxRetriesExceeded` exception.
    *   Test it on a function that randomly raises `ConnectionError`.
3.  **Role-Based Access Control (RBAC):** Write a decorator `@requires_role('admin')` that checks a global (mocked) `current_user` dict. If the role doesn't match, raise `PermissionError`.

---

### Day 4: Context Managers & Magic Methods
*Why? Clean resource management (DB connections, File locks) is mandatory.*

**Topics:**
*   The `with` statement internals (`__enter__`, `__exit__`).
*   `contextlib` module (`contextmanager` decorator).
*   Important Magic Methods: `__call__`, `__getitem__`, `__len__`, `__str__` vs `__repr__`.

**Practical Tasks:**
1.  **Atomic Transaction Simulator:** Create a class `MockDatabaseSession`.
    *   `__enter__`: prints "Starting transaction..."
    *   `__exit__`: If no exception, print "Commit". If exception occurs, print "Rollback" and suppress the exception (or re-raise based on config).
2.  **Safe File Writer:** Write a Context Manager `SafeWriter` that writes to a temporary file first. Only on successful exit (no errors) does it rename the temp file to the target filename. (This prevents corrupted files if the script crashes mid-write).
3.  **Callable Class:** Create a class `CurrencyConverter` that is initialized with rates, but can be called like a function: `convert(amount, "USD", "EUR")`. Use `__call__`.

---

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

---

### Days 6-7: Weekend Project - "The Resilient Processor"
*Combine everything into a cohesive mini-system.*

**Scenario:** You need to process a batch of payment files (JSON format) and save valid ones to a "Database" (a list in memory), while logging errors.

**Requirements:**
1.  **Input:** Generate a file with 10,000 JSON objects. Some are valid, some have missing fields, some have negative amounts.
2.  **Generator Pipeline:** Create a generator that reads the file efficiently.
3.  **Validation:** Use **Pydantic** to validate each record.
4.  **Resilience:** Use your `@retry` decorator on the function that simulates saving to the DB (make it randomly fail 10% of the time).
5.  **Safety:** Use a **Context Manager** to ensure the "Report File" (where you write results: "Success: 9000, Failed: 1000") is properly closed even if the script crashes.
6.  **Decorators:** Apply your `@timeit` decorator to measure the total processing time.

---

**Resources for Week 1:**
*   *Real Python:* "Python Memory Management", "Primers on Decorators/Generators".
*   *Book:* "Fluent Python" (Chapters on Data Model and Object References) — *highly recommended for Middle level*.
*   *Docs:* Pydantic V2 official docs.
