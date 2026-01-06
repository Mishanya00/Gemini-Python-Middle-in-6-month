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