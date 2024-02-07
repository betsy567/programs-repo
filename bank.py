class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_account_info(self):
        print(f"Account Information:\nAccount Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nAccount Type: {self.account_type}\nBalance: ${self.balance}")

# Example usage:
account1 = BankAccount(account_number="123456", account_holder_name="John Doe", account_type="Savings", balance=1000)

account1.display_account_info()
account1.deposit(500)
account1.withdraw(200)
