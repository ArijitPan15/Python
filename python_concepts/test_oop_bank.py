import unittest
from decimal import Decimal
from oop_bank import BankAccount


class BankTests(unittest.TestCase):
    def test_deposit_withdraw(self):
        account = BankAccount("Alex", "100")
        account.deposit("25.50")
        account.withdraw("20")
        self.assertEqual(account.balance, Decimal("105.50"))
        self.assertEqual(len(account.transactions), 3)

    def test_transfer(self):
        first = BankAccount("A", "50")
        second = BankAccount("B")
        first.transfer_to(second, "15")
        self.assertEqual(first.balance, Decimal("35"))
        self.assertEqual(second.balance, Decimal("15"))

    def test_validation(self):
        account = BankAccount("A")
        for amount in ("-1", "NaN", "Infinity", "0"):
            with self.subTest(amount=amount):
                with self.assertRaises(ValueError):
                    account.deposit(amount)
        with self.assertRaises(ValueError):
            account.withdraw(1)


if __name__ == "__main__":
    unittest.main()
