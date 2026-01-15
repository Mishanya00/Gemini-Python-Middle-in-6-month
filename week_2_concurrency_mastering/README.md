# Week 2: Mastering Concurrency (AsyncIO & Threading)
**Focus:** Deep understanding of the Event Loop, asynchronous design patterns, and handling CPU-bound operations in a non-blocking way.
**Goal:** Build a high-performance async application that doesn't freeze under load and manages shared resources safely.

---

### Day 1: The Event Loop & The Cost of Blocking
*Why? One blocking call (like `requests.get` or complex math) kills the performance of the entire FastAPI server.*

**Topics:**
*   Cooperative Multitasking vs Preemptive Multitasking.
*   The Event Loop anatomy (Tasks, Futures, Coroutines).
*   `asyncio.run()`, `asyncio.create_task()`.
*   **The Golden Rule:** Never block the loop.
*   Difference between `time.sleep()` (blocks everything) and `asyncio.sleep()` (yields control).

**Practical Tasks:**
1.  **The Freezer:** Write an async program that launches 3 tasks. Inside one task, use `time.sleep(5)`. Observe how the other two tasks stop executing during that time. Fix it using `asyncio.sleep(5)`.
2.  **Poller Simulation:** Write a loop that checks a "status" every 1 second. While waiting, the program should be able to accept user input or print "Heartbeat".
3.  **Debug Mode:** Enable `asyncio` debug mode (`PYTHONASYNCIODEBUG=1`) and write a deliberately slow callback to see how Python warns you about "Blocking operations".

---

### Day 2: Structured Concurrency & Error Handling
*Why? Firing tasks into the void (`fire-and-forget`) leads to memory leaks and silent failures.*

**Topics:**
*   `asyncio.gather()` vs `TaskGroup` (Python 3.11+ modern standard).
*   Handling exceptions in concurrent tasks (`return_exceptions=True` in gather).
*   Cancelling tasks and handling `CancelledError`.
*   Timeouts (`asyncio.wait_for`).

**Practical Tasks:**
1.  **Batch API Fetcher:** Simulate fetching user data for 10 user IDs concurrently.
    *   3 requests should succeed.
    *   1 request should raise a generic Exception.
    *   1 request should "hang" (simulate network lag).
    *   **Goal:** Use `asyncio.wait_for` to kill the hanging request after 2 seconds, and ensure the Exception doesn't crash the whole batch. Print results for the successful ones.
2.  **Graceful Shutdown:** Write a script with a long-running background task. Handle `KeyboardInterrupt` (Ctrl+C) to cancel the task properly and print "Cleanup complete" before exiting.

---

### Day 3: Synchronization Primitives (Thread-Safety in Async)
*Why? Race conditions in async code result in double-spending or corrupted balances.*

**Topics:**
*   Shared state in AsyncIO.
*   `asyncio.Lock` (Mutual exclusion).
*   `asyncio.Semaphore` (Limiting concurrency/Rate limiting).
*   `asyncio.Event` (Signaling between tasks).

**Practical Tasks:**
1.  **The Double-Spend Attack:** Create a `BankAccount` class with `balance = 100`.
    *   Write an async function `withdraw(amount)` that: reads balance -> `await asyncio.sleep(0.1)` (simulate DB lag) -> updates balance.
    *   Launch 5 concurrent withdrawals of 50.
    *   Observe the balance going negative or being inconsistent.
    *   **Fix:** Use `asyncio.Lock` to ensure data integrity.
2.  **Rate Limiter:** You have an external API that allows only 3 requests per second. Write a client using `asyncio.Semaphore(3)` that processes 20 requests. Observe how they are processed in batches of 3.

---

### Day 4: CPU-bound vs IO-bound (Processes vs Threads vs Async)
*Why? Async is for IO. If you calculate crypto-hashes or resize images in Async, your server dies. You need Executors.*

**Topics:**
*   GIL (Global Interpreter Lock) revisited: Why Async doesn't help with CPU tasks.
*   `concurrent.futures.ThreadPoolExecutor` (for blocking IO like file operations).
*   `concurrent.futures.ProcessPoolExecutor` (for CPU heavy tasks).
*   `loop.run_in_executor`.

**Practical Tasks:**
1.  **The Heavy Calculator:** Create an async web server (simulated with a loop) that handles requests.
    *   Request A: Returns "Pong" immediately.
    *   Request B: Calculates `sum(i*i for i in range(10**7))` (CPU heavy).
    *   Problem: Request B blocks Request A.
    *   **Fix:** Offload the calculation to a `ProcessPoolExecutor`.
2.  **File Reader:** Read 5 large text files. Use `ThreadPoolExecutor` via `run_in_executor` to read them without freezing the main event loop.

---

### Day 5: Async Context Managers & Iterators
*Why? Advanced streaming of data and resource management in modern Python.*

**Topics:**
*   `__aenter__` and `__aexit__`.
*   `__aiter__` and `__anext__`.
*   `contextvars` (Critical for request-scoped data like `TraceID` in async apps).

**Practical Tasks:**
1.  **Async DB Connection:** Mock a database connection class using `async with`.
    *   Connect (async sleep), Do work, Disconnect (async sleep).
2.  **Streaming Ticker:** Create an async generator that yields random stock prices every 0.5 seconds.
    *   Consume this generator in a loop and stop if the price drops below a threshold.
3.  **Context Context:** Use `contextvars` to store a "Request ID". Launch 3 concurrent tasks, each setting a different Request ID. Inside a nested function (that takes no arguments), print the current Request ID. Prove that they don't overwrite each other.

---

### Days 6-7: Weekend Project - "High-Frequency Crypto Aggregator"
*A simplified version of a real finance-related task.*

**Scenario:** You need to aggregate prices from 3 different crypto exchanges (simulated), calculate the average, and save it, while handling rate limits and heavy calculations.

**Requirements:**
1.  **Exchange Simulator:** Create 3 functions representing exchanges. They respond with random delays. One occasionally throws errors.
2.  **Concurrent Fetching:** Fetch prices from all 3 exchanges simultaneously (use `gather` or `TaskGroup`). Handle errors (if one fails, ignore it and average the others).
3.  **Rate Limiting:** Ensure you don't hit the "exchanges" more than 5 times per second (Semaphore).
4.  **CPU Heavy Analysis:** Every time you get new prices, calculate a "Volatility Index" (simulate a heavy math function). run this in a **ProcessPool** so it doesn't slow down the fetching.
5.  **Storage:** Write the results to a file using a non-blocking approach (ThreadExecutor or async file lib like `aiofiles` if you want to install it, otherwise `run_in_executor`).
6.  **Architecture:** Clean code, type hints, and proper `main()` entry point.

---

**Resources for Week 2:**
*   *Real Python:* "Async IO in Python: A Complete Walkthrough".
*   *Video:* "ArjanCodes: Next Level Python AsyncIO".
*   *Documentation:* Python `asyncio` official docs (sections on Streams and Synchronization).

**Совет на эту неделю:**
Самая частая ошибка при переходе на Middle — непонимание, где использовать `ProcessPool`, а где `ThreadPool`.
*   Если задача **ждет** (сеть, диск, БД) -> `AsyncIO` (или `ThreadPool` если библиотека старая).
*   Если задача **думает** (математика, парсинг JSON огромного, обработка фото) -> `ProcessPool`.

Удачи! Жду отчета, как справишься с "Double-Spend Attack".