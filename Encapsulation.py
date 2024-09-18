from abc import ABC, abstractmethod  # For Abstraction

# Encapsulation
class Account:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self.__balance = balance  # Private attribute

    # Method to get balance (Encapsulation: providing controlled access)
    def get_balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

# Inheritance and Abstraction
class BankAccount(ABC):
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner

    @abstractmethod
    def account_info(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

# Subclass inheriting from BankAccount
class SavingsAccount(BankAccount):
    interest_rate = 0.03  # 3% interest

    def __init__(self, account_number, owner, balance):
        super().__init__(account_number, owner)
        self.__balance = balance

    def account_info(self):
        return f"Savings Account - Owner: {self.owner}, Balance: {self.__balance}"

    # Polymorphism: Method overriding
    def calculate_interest(self):
        return self.__balance * self.interest_rate

# Another Subclass inheriting from BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, balance):
        super().__init__(account_number, owner)
        self.__balance = balance

    def account_info(self):
        return f"Checking Account - Owner: {self.owner}, Balance: {self.__balance}"

    # Polymorphism: Method overriding
    def calculate_interest(self):
        return 0  # Checking accounts have no interest

# Testing the code

# Encapsulation example
my_account = Account("John", 1000)
print(my_account.get_balance())  # Accessing private variable through a method
my_account.deposit(500)
my_account.withdraw(200)

# Inheritance, Polymorphism, and Abstraction example
savings = SavingsAccount("12345", "John", 5000)
checking = CheckingAccount("67890", "John", 3000)

# Abstract methods being implemented by subclasses
print(savings.account_info())
print(f"Savings interest: {savings.calculate_interest()}")

print(checking.account_info())
print(f"Checking interest: {checking.calculate_interest()}")
