#Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on the data into a single unit, or class. 

#It restricts direct access to some of the object's components, which can help prevent accidental interference and misuse.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
    

account = BankAccount("Sahil", 1000)
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())