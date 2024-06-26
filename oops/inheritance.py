
#Inheritance is a mechanism where a new class inherits attributes and methods from an existing class. 
#It promotes code reuse and establishes a relationship between classes.


class Animal: #parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal): #child class
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal): #child class
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
