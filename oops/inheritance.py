# Inheritance is a key concept in OOP where a new class (subclass or derived class) can inherit attributes and methods from an existing class (superclass or base class).


# Base class
class Animal():
    def __init__(self, name):
        self.name = name

        def speak(self):
            raise NotImplementedError("Subclass must implement this method")
        
# derived class
class Dog(Animal):
    def speak(self):
        return f"{se}"