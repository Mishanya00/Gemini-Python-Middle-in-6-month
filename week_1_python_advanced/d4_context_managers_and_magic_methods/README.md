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