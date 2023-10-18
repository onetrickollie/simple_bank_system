# test_bank_system.py

import unittest
from bank_system import BankAccount
from bank_exceptions import InsufficientFundsError, NegativeAmountError

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(101, "Alice", 1000)

    def test_deposit_positive_amount(self):
        result = self.account.deposit(500)
        # Round to 2 decimal places for comparison
        result = round(float(result.split("$")[-1].split(" ")[0]), 2)
        expected = round(1500.0, 2)
        self.assertEqual(result, expected)

    def test_deposit_negative_amount(self):
        with self.assertRaises(NegativeAmountError) as context:
            self.account.deposit(-200)
        self.assertEqual(str(context.exception), "Amount cannot be negative: $-200")

    def test_withdraw_positive_amount(self):
        result = self.account.withdraw(200)
        # Round to 2 decimal places for comparison
        result = round(float(result.split("$")[-1].split(" ")[0]), 2)
        expected = round(800.0, 2)
        self.assertEqual(result, expected)

    def test_get_balance(self):
        result = self.account.get_balance()
        # Round to 2 decimal places for comparison
        result = round(float(result.split("$")[-1].split(" ")[0]), 2)
        expected = round(1000.0, 2)
        self.assertEqual(result, expected)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError) as context:
            self.account.withdraw(2000)
        self.assertEqual(str(context.exception), "Insufficient funds. You tried to withdraw $2000, but your balance is only $1000.")

    def test_withdraw_negative_amount(self):
        with self.assertRaises(NegativeAmountError) as context:
            self.account.withdraw(-200)
        self.assertEqual(str(context.exception), "Amount cannot be negative: $-200")

if __name__ == '__main__':
    unittest.main()
