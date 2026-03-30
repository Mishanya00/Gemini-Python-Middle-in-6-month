### Day 1: Memory Management & Mutability

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