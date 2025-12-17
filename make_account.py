def make_account(initial_balance):
    if not isinstance(initial_balance, (int, float)):
        raise TypeError("initial_balance must be a number")

    balance = float(initial_balance)

    def deposit(amount):
        nonlocal balance
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            raise ValueError("amount must be positive")
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > balance:
            raise ValueError("insufficient funds")
        balance -= amount
        return balance

    return deposit, withdraw

