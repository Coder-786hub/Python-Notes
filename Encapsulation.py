# Encapsulation is one of the fundamental principles of object-oriented programming (OOP). It refers to restricting access to certain details of an object to protect its integrity and prevent unintended interference. In Python, encapsulation is achieved through access modifiers such as public, protected, and private attributes.


# Public Attributes:
# Accessible from anywhere.
# No leading underscores.

class Demo:
    def __init__(self):
        self.value = 10  # Public attribute

obj = Demo()
print(obj.value)  # Accessible from outside the class

# Protected Attributes:
# Denoted by a single leading underscore (_).
# Suggests that the attribute is for internal use, but it can still be accessed outside the class.

class Demo:
    def __init__(self):
        self._value = 20  # Protected attribute

obj = Demo()
print(obj._value)  # Not recommended but accessible

# Private Attributes:
# Denoted by a double leading underscore (__).
# Python applies name mangling to make these attributes inaccessible directly from outside the class.
# They can still be accessed through their mangled names (not recommended).

class Demo: 
    def __init__(self):
        self.__value = 30  # Private attribute

obj = Demo()
print(obj.__value)  # Raises AttributeError
print(obj._Demo__value)  # Access using mangled name (not recommended)


# Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid or insufficient funds.")

    def get_balance(self):
        return self.__balance  # Controlled access to private data

# Usage
account = BankAccount(1000)
account.deposit(500)          # Deposited: 500
account.withdraw(300)         # Withdrawn: 300
print(account.get_balance())  # 1200

# Direct access is restricted
print(account.__balance)      # AttributeError
