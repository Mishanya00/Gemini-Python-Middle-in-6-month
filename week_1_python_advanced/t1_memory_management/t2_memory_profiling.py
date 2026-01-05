import sys
import time
from dataclasses import dataclass
from pympler import asizeof  # pip install pympler
import gc


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonSlots:
    __slots__ = ("name", "age")
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Transaction:
    def __init__(self, transaction_id, amount, currency, timestamp,
                 sender, receiver, status, category, description, metadata):
        self.transaction_id = transaction_id
        self.amount = amount
        self.currency = currency
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.status = status
        self.category = category
        self.description = description
        self.metadata = metadata


class TransactionSlots:
    __slots__ = ['transaction_id', 'amount', 'currency', 'timestamp',
                 'sender', 'receiver', 'status', 'category', 'description', 'metadata']

    def __init__(self, transaction_id, amount, currency, timestamp,
                 sender, receiver, status, category, description, metadata):
        self.transaction_id = transaction_id
        self.amount = amount
        self.currency = currency
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
        self.status = status
        self.category = category
        self.description = description
        self.metadata = metadata


from collections import namedtuple

TransactionNamedTuple = namedtuple('TransactionNamedTuple',
                                   ['transaction_id', 'amount', 'currency', 'timestamp', 'sender',
                                    'receiver', 'status', 'category', 'description', 'metadata'])


def create_transactions_regular(n=1000000):
    print(f"\n{'=' * 60}")
    print(f"Creating {n} regular class instances...")

    gc.collect()
    start_memory = asizeof.asizeof([])
    start_time = time.time()

    transactions = []
    for i in range(n):
        transaction = Transaction(
            transaction_id=f"txn_{i}",
            amount=100.0 + (i % 1000),
            currency="USD",
            timestamp=f"2024-01-{i % 30 + 1:02d} 10:00:00",
            sender=f"sender_{i % 10000}",
            receiver=f"receiver_{i % 10000}",
            status="completed" if i % 2 == 0 else "pending",
            category="payment",
            description=f"Transaction #{i}",
            metadata={"index": i, "batch": i // 1000}
        )
        transactions.append(transaction)

    end_time = time.time()
    end_memory = asizeof.asizeof(transactions)

    total_memory_used = end_memory - start_memory
    true_avg_per_instance = total_memory_used / n

    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"List memory: {(end_memory - start_memory) / 1024 / 1024:.2f} MB")
    print(f"True average per instance: {true_avg_per_instance:.2f} bytes")
    print(f"Single instance measurement: {asizeof.asizeof(transactions[0])} bytes")
    return transactions


def create_transactions_slots(n=1000000):
    print(f"\n{'=' * 60}")
    print(f"Creating {n} __slots__ class instances...")

    gc.collect()
    start_memory = asizeof.asizeof([])
    start_time = time.time()

    transactions = []
    for i in range(n):
        transaction = TransactionSlots(
            transaction_id=f"txn_{i}",
            amount=100.0 + (i % 1000),
            currency="USD",
            timestamp=f"2024-01-{i % 30 + 1:02d} 10:00:00",
            sender=f"sender_{i % 10000}",
            receiver=f"receiver_{i % 10000}",
            status="completed" if i % 2 == 0 else "pending",
            category="payment",
            description=f"Transaction #{i}",
            metadata={"index": i, "batch": i // 1000}
        )
        transactions.append(transaction)

    end_time = time.time()
    end_memory = asizeof.asizeof(transactions)
    total_memory_used = end_memory - start_memory
    true_avg_per_instance = total_memory_used / n

    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"List memory: {(end_memory - start_memory) / 1024 / 1024:.2f} MB")
    print(f"True average per instance: {true_avg_per_instance:.2f} bytes")
    print(f"Single instance measurement: {asizeof.asizeof(transactions[0])} bytes")
    return transactions


def create_transactions_namedtuple(n=1000000):
    print(f"\n{'=' * 60}")
    print(f"Creating {n} namedtuple instances...")

    gc.collect()
    start_memory = asizeof.asizeof([])
    start_time = time.time()

    transactions = []
    for i in range(n):
        transaction = TransactionNamedTuple(
            transaction_id=f"txn_{i}",
            amount=100.0 + (i % 1000),
            currency="USD",
            timestamp=f"2024-01-{i % 30 + 1:02d} 10:00:00",
            sender=f"sender_{i % 10000}",
            receiver=f"receiver_{i % 10000}",
            status="completed" if i % 2 == 0 else "pending",
            category="payment",
            description=f"Transaction #{i}",
            metadata={"index": i, "batch": i // 1000}
        )
        transactions.append(transaction)

    end_time = time.time()
    end_memory = asizeof.asizeof(transactions)
    total_memory_used = end_memory - start_memory
    true_avg_per_instance = total_memory_used / n

    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"List memory: {(end_memory - start_memory) / 1024 / 1024:.2f} MB")
    print(f"True average per instance: {true_avg_per_instance:.2f} bytes")
    print(f"Single instance measurement: {asizeof.asizeof(transactions[0])} bytes")
    return transactions


def create_persons_regular(n=1000000):
    print(f"\n{'=' * 60}")
    print(f"Creating {n} Person regular class instances...")

    gc.collect()
    start_memory = asizeof.asizeof([])
    start_time = time.time()

    persons = []
    for i in range(n):
        person = Person(
            name=f"Person_{i}",
            age=i % 100
        )
        persons.append(person)

    end_time = time.time()
    end_memory = asizeof.asizeof(persons)

    total_memory_used = end_memory - start_memory
    true_avg_per_instance = total_memory_used / n

    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"List memory: {(end_memory - start_memory) / 1024 / 1024:.2f} MB")
    print(f"True average per instance: {true_avg_per_instance:.2f} bytes")
    print(f"Single instance measurement: {asizeof.asizeof(persons[0])} bytes")
    return persons


def create_persons_slots(n=1000000):
    print(f"\n{'=' * 60}")
    print(f"Creating {n} Person __slots__ class instances...")

    gc.collect()
    start_memory = asizeof.asizeof([])
    start_time = time.time()

    persons = []
    for i in range(n):
        person = PersonSlots(
            name=f"Person_{i}",
            age=i % 100
        )
        persons.append(person)

    end_time = time.time()
    end_memory = asizeof.asizeof(persons)

    total_memory_used = end_memory - start_memory
    true_avg_per_instance = total_memory_used / n

    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"List memory: {(end_memory - start_memory) / 1024 / 1024:.2f} MB")
    print(f"True average per instance: {true_avg_per_instance:.2f} bytes")
    print(f"Single instance measurement: {asizeof.asizeof(persons[0])} bytes")
    return persons


# Add namedtuple for Person
PersonNamedTuple = namedtuple('PersonNamedTuple', ['name', 'age'])

def create_persons_namedtuple(n=1000000):
    print(f"\n{'=' * 60}")
    print(f"Creating {n} Person namedtuple instances...")

    gc.collect()
    start_memory = asizeof.asizeof([])
    start_time = time.time()

    persons = []
    for i in range(n):
        person = PersonNamedTuple(
            name=f"Person_{i}",
            age=i % 100
        )
        persons.append(person)

    end_time = time.time()
    end_memory = asizeof.asizeof(persons)

    total_memory_used = end_memory - start_memory
    true_avg_per_instance = total_memory_used / n

    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"List memory: {(end_memory - start_memory) / 1024 / 1024:.2f} MB")
    print(f"True average per instance: {true_avg_per_instance:.2f} bytes")
    print(f"Single instance measurement: {asizeof.asizeof(persons[0])} bytes")
    return persons


def main():
    print("MEMORY PROFILING DEMONSTRATION")
    print("Comparing Person (2 fields) vs Transaction (10 fields) classes")

    sample_size = 100000

    print("\n" + "=" * 60)
    print("TESTING PERSON CLASS (2 fields)")
    print("=" * 60)

    try:
        regular_persons = create_persons_regular(sample_size)
        del regular_persons
        gc.collect()
    except MemoryError:
        print("Not enough memory for Person regular class test")

    try:
        slots_persons = create_persons_slots(sample_size)
        del slots_persons
        gc.collect()
    except MemoryError:
        print("Not enough memory for Person slots test")

    try:
        tuple_persons = create_persons_namedtuple(sample_size)
        del tuple_persons
        gc.collect()
    except MemoryError:
        print("Not enough memory for Person namedtuple test")

    print("\n" + "=" * 60)
    print("TESTING TRANSACTION CLASS (10 fields)")
    print("=" * 60)

    try:
        regular_txns = create_transactions_regular(sample_size)
        del regular_txns
        gc.collect()
    except MemoryError:
        print("Not enough memory for Transaction regular class test")

    try:
        slots_txns = create_transactions_slots(sample_size)
        del slots_txns
        gc.collect()
    except MemoryError:
        print("Not enough memory for Transaction slots test")

    try:
        tuple_txns = create_transactions_namedtuple(sample_size)
        del tuple_txns
        gc.collect()
    except MemoryError:
        print("Not enough memory for Transaction namedtuple test")


if __name__ == "__main__":
    main()