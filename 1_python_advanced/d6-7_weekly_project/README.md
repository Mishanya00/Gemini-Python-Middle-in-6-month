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