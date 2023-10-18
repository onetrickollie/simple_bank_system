#Kaixiang Liu
#884780172
#10/18/2023
#lab7

from bank_exceptions import InsufficientFundsError, NegativeAmountError

class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError(amount)
        self.balance += amount
        return f"${amount} deposited, New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        if amount < 0:
            raise NegativeAmountError(amount)
        

        self.balance -= amount
        return (f"${amount} withdrawn, New balance: ${self.balance}")


    def get_balance(self):
        return (f"Account balance for {self.account_holder}: ${self.balance}")


def main():
    alice_account = BankAccount(101, "Alice", 1000)
    bob_account = BankAccount(102, "Bob", 500)
    while True:
        print("\n1: Deposit")
        print("2: Withdraw")
        print("3: Check Balance")
        print("4: Exit")

        userInp = input("Enter your choice: ")

        if userInp == '1':
            try:
                amount = float(input("Enter deposit amount: $"))
                print(alice_account.deposit(amount))
            except NegativeAmountError as e:
                print(e)
            except ValueError:
                print("Enter a valid number.")

        elif userInp == '2':
            try:
                amount = float(input("Enter withdrawal amount: $"))
                print(alice_account.withdraw(amount))
            except InsufficientFundsError as e:
                print(e)
            except NegativeAmountError as e:
                print(e)
            except ValueError:
                print("Enter a valid number.")

        elif userInp == '3':
            print(alice_account.get_balance())

        elif userInp == '4':
            print("Exiting")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":

    main()