# Week 3: Advanced OOP, Interfaces & Design Patterns
**Focus:** Decoupling code, enforcing contracts (Interfaces/Protocols), and applying GoF patterns in a Pythonic way.
**Goal:** Write code that is easy to extend (Open/Closed Principle) and easy to test.

### Prerequisites
*   Understanding of basic Classes and Inheritance.
*   Completed Weeks 1 & 2.

---

### Day 1: The Power of Abstraction (ABCs vs Protocols)
*Why? In Fintech, you need strict contracts. A "Payment Processor" must implement `pay()` and `refund()`. You can't rely on "trust me bro".*

**Topics:**
*   **Abstract Base Classes (ABC):** `abc.ABC`, `@abstractmethod`. Enforcing structure via inheritance.
*   **Duck Typing & Protocols:** `typing.Protocol` (Python 3.8+). Structural subtyping (Go-style interfaces). Why Protocols are often better than ABCs in modern Python.
*   **Liskov Substitution Principle (LSP):** Subclasses must be swappable for their parents without breaking the app.

**Practical Tasks:**
1.  **The Contract:** Define a `NotificationSender` Protocol with a method `send(user_id: int, message: str) -> bool`.
2.  **Implementations:** Create concrete classes `EmailSender` and `SMSSender` that implement this Protocol.
3.  **Dependency Injection:** Write a function `alert_user(sender: NotificationSender, user_id: int)` that works with *any* class adhering to the Protocol. Try passing a class that *doesn't* have the `send` method and see Mypy/IDE yell at you.

---

### Day 2: Advanced Inheritance (Mixins & MRO)
*Why? You want to share functionality (like "logging" or "to_dict") across many unrelated models without creating a monster "God Class".*

**Topics:**
*   **MRO (Method Resolution Order):** How Python decides which method to call in multiple inheritance (`super()` mechanics). C3 Linearization.
*   **Mixins:** Small classes that add specific behavior (e.g., `TimestampMixin`, `JsonSerializableMixin`).
*   **Composition over Inheritance:** When *not* to use inheritance.

**Practical Tasks:**
1.  **The Mixin:** Create a `JsonLoggableMixin` with a method `log_state()` that dumps `self.__dict__` to JSON.
2.  **The Hierarchy:** Create a base class `BankAccount`. Create subclasses `SavingsAccount` and `CreditAccount`.
3.  **The Application:** Add `JsonLoggableMixin` to `SavingsAccount` but not `CreditAccount`. Verify `SavingsAccount` can log itself.
4.  **Diamond Problem:** Create a diamond inheritance structure (A -> B, A -> C, D inherits B and C). Override a method in all of them. Call it from D. Inspect `D.__mro__` to understand the execution order.

---

### Day 3: Creational Patterns (Singleton, Factory, Builder)
*Why? DB connections should be reused (Singleton). Creating complex objects (like a Report with 50 settings) needs structure (Builder).*

**Topics:**
*   **Singleton:** The Pythonic way (Modules are Singletons!) vs The Class way (`__new__`, Metaclasses). Use cases: Config, DB Pools.
*   **Factory Method:** Creating objects without specifying the exact class (e.g., `get_payment_gateway("stripe")`).
*   **Builder:** Constructing complex objects step-by-step.

**Practical Tasks:**
1.  **Config Singleton:** Create a `Settings` class that parses `.env` files. Ensure that no matter how many times you initialize `Settings()`, you get the *exact same instance* (use `__new__`).
2.  **Payment Factory:** Create a function `get_payment_processor(method: str)`.
    *   If `method == "card"`, return a `StripeProcessor`.
    *   If `method == "crypto"`, return a `BinanceProcessor`.
    *   Both must follow a common Protocol.

---

### Day 4: Behavioral Patterns (Strategy & Observer)
*Why? This is the bread and butter of Fintech business logic.*

**Topics:**
*   **Strategy Pattern:** Swapping algorithms at runtime. (e.g., "Calculate Tax for US" vs "Calculate Tax for Dubai").
*   **Observer Pattern:** Event-driven architecture within the app. (e.g., "When User Registers -> Send Email AND Create Wallet AND Notify Admin").
*   **Refactoring `if/else` hell:** Replacing massive `if type == 'A'... elif type == 'B'` blocks with Strategy.

**Practical Tasks:**
1.  **Tax Strategy:** Create a `TaxCalculator` class that takes a `strategy` argument.
    *   Implement `USTaxStrategy` (10%) and `UAEStrategy` (0%).
    *   Process a transaction using both strategies without changing the code of the transaction logic itself.
2.  **Event System:** Create a simple `EventManager`.
    *   Allow subscribers to `subscribe("event_name", callback_function)`.
    *   Allow publishers to `emit("event_name", data)`.
    *   Scenario: When `emit("payment_received")` happens, trigger two independent functions: `update_balance` and `send_receipt`.

---

### Day 5: Structural Patterns (Adapter & Decorator)
*Why? You will integrate with terrible 3rd party APIs. Adapters make them look nice in your code.*

**Topics:**
*   **Adapter:** Making incompatible interfaces work together. (Wrapping a weird XML SOAP library to look like a nice JSON library).
*   **Decorator (as a Pattern):** We learned Python Decorators in Week 1. Now understand the *Class-based* Decorator pattern (wrapping objects to extend behavior dynamically).
*   **Facade:** Providing a simple interface to a complex subsystem.

**Practical Tasks:**
1.  **The Legacy Adapter:** Imagine a legacy library `OldBank` with method `transfer_money_xml(xml_string)`.
    *   Write an `OldBankAdapter` that implements your modern `PaymentProtocol` (`pay(amount, currency)`).
    *   Inside the adapter, convert the clean data into the ugly XML required by the legacy lib.
2.  **Service Facade:** You have 3 complex subsystems: `UserSystem`, `WalletSystem`, `KYCSystem`.
    *   Create a `OnboardingFacade` with one method `register_user(...)` that orchestrates calls to all three systems in the correct order.

---

### Days 6-7: Weekend Project - "The Fintech Fraud Engine"
*Consolidating OOP, Strategies, and Factories.*

**Scenario:** You are building a fraud detection system for your startup. Transactions pass through a series of "Rules". If any rule is violated, the transaction is rejected.

**Requirements:**
1.  **Protocol:** Define a `FraudRule` protocol with a method `check(transaction: dict) -> bool`.
2.  **Strategies (Rules):** Implement 3 rules:
    *   `AmountLimitRule`: Rejects if amount > 10,000.
    *   `BlacklistCountryRule`: Rejects if country is in a forbidden list.
    *   `VelocityRule`: (Mocked) Rejects if user made > 3 transactions in 1 minute.
3.  **The Engine (Composite/Observer):** Create a `FraudEngine`.
    *   It should accept a list of rules (List of Strategies).
    *   Method `verify_transaction(tx)` iterates through all rules.
    *   If a rule fails, raise a custom exception `FraudDetected(reason)`.
4.  **Factory:** Create a generic way to load these rules (e.g., from a config list of strings `["AmountLimit", "Blacklist"]`).
5.  **Tests:** Demonstrate that you can add a NEW rule (e.g., `WeekendRule`) without touching the code of the `FraudEngine`.

---

**Resources for Week 3:**
*   *Website:* **Refactoring.guru** (Design Patterns in Python) — *This is the bible for patterns. Read the Python examples specifically.*
*   *Video:* "ArjanCodes: Python Dependency Injection" and "Strategy Pattern".
*   *Article:* "Hynek Schlawack: Python Interfaces (Protocols)".

**Совет:**
В середине этой недели тебе может показаться, что ты "over-engineering" (усложняешь).
*   "Зачем мне Factory, если я могу просто сделать `if`?"
*   "Зачем мне Protocol, если я знаю, что передаю?"
Это нормальная реакция. На маленьких скриптах это действительно лишнее. Но как только проект вырастает до 50+ файлов и над ним работают 3 человека, без этих паттернов проект превращается в лапшу (Spaghetti Code). В Финтехе цена ошибки высока, поэтому структура важнее скорости написания первой версии.

Удачи с паттернами! Жду реализации Fraud Engine.