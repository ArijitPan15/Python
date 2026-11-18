"""Bank account OOP exercise with encapsulation and transaction history."""
from decimal import Decimal, InvalidOperation


class BankAccount:
    def __init__(self, owner, opening_balance="0"):
        if not owner.strip():
            raise ValueError("owner is required")
        self.owner = owner.strip()
        self._balance = Decimal("0")
        self._transactions = []
        opening = self._amount(opening_balance, allow_zero=True)
        if opening:
            self.deposit(opening)

    @staticmethod
    def _amount(value, allow_zero=False):
        try:
            amount = Decimal(str(value))
        except (InvalidOperation, ValueError):
            raise ValueError("invalid amount") from None
        if not amount.is_finite() or amount < 0 or (amount == 0 and not allow_zero):
            raise ValueError("amount must be positive and finite")
        return amount

    @property
    def balance(self):
        return self._balance

    @property
    def transactions(self):
        return tuple(self._transactions)

    def deposit(self, amount):
        amount = self._amount(amount)
        self._balance += amount
        self._transactions.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount):
        amount = self._amount(amount)
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        self._transactions.append(("withdrawal", amount))
        return self._balance

    def transfer_to(self, recipient, amount):
        if not isinstance(recipient, BankAccount):
            raise TypeError("recipient must be a BankAccount")
        if recipient is self:
            raise ValueError("cannot transfer to same account")
        amount = self._amount(amount)
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self.withdraw(amount)
        recipient.deposit(amount)
