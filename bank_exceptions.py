# bank_exceptions.py

class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        message = "Insufficient funds. You tried to withdraw ${}, but your balance is only ${}.".format(self.amount, self.balance)
        super().__init__(message)

class NegativeAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount
        message = f"Amount cannot be negative: ${self.amount}"
        super().__init__(message)
