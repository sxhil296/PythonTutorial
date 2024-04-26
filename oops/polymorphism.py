# Polymorphism is the ability of different objects to respond to the same method or function in different ways. In Python, polymorphism is achieved through method overriding and method overloading.


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(make_animal_speak(dog))  # Output: Woof!
print(make_animal_speak(cat))  # Output: Meow!


# In this example, we have a base class `Animal` with a method `speak()`. The `Dog` and `Cat` classes inherit from the `Animal` class and override the `speak()` method with their own implementations. The `make_animal_speak()` function takes an `Animal` object as a parameter and calls the `speak()` method on it.

# When we call `make_animal_speak()` with a `Dog` object, it returns "Woof!", and when we call it with a `Cat` object, it returns "Meow!". This is an example of polymorphism in Python, where different objects respond to the same method (`speak()`) in different ways.


# Types of polymorphism

# Compile-time polymorphism (aka Method Overloading)
# it is the ability to define multiple methods with the same name in the same class but with different parameters

# python does not support this by default, as it does not allow methods with same name in a class.
# however we can achieve this in python using default parameter values and variable length arguments.
class MathOperations:
    def add(self, a, b=0):
        return a + b

math = MathOperations()
print(math.add(2))      # Output: 2
print(math.add(2, 3))   # Output: 5  


# run time polymorphism (aka method overriding)
# redefining a method in the subclass with same name and parameters
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
animal.speak()  # Output: Animal speaks

dog = Dog()
dog.speak()     # Output: Dog barks

# the speak method in the Dog class overrides the speak method in the Animal class, demonstrating run-time polymorphism or method overriding
