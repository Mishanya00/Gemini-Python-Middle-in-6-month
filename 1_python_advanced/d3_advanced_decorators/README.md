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