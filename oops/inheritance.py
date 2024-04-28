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
        return f"{self.name} says Woof!"
    
# derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    


# object or instance creation
dog = Dog("Dog")
cat = Cat("Cat")

# call the speak method
print(dog.speak())
print(cat.speak())

