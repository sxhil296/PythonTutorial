# OOPS - Object Oriented Programming System 
- Object-Oriented Programming (OOP) is a programming paradigm that organizes code around the concept of "objects," which are instances of classes.
- in OOP, we organize our code into objects that represent real-world entities. These objects have attributes (data) and methods (functions) that operate on the data.

## Class
- Class is a blueprint or template for creating objects.
- It defines attributes (properties) and methods (functions) that objects of the class will have.
  
## Object
- Object is an instance of a class.
- It represents a real-world entity with attributes(data) and behaviors(methods).

## Instance
- A specific occurrence of an object created from a class.

## Method
- A function or behavior associated with an object.

```
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The car is starting.")

    def stop(self):
        print("The car is stopping.")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes and calling methods
print(my_car.make)
my_car.start()
my_car.stop()
```
- dot notation is used to access attributes and methods of an object 
  ```
  object_name.attribute_name
  object_name.method_name()
  ```


# Pillars of OOPS
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

## Encapsulation
- bundling of data (attributes) and methods (functions) that operate on that data into a single unit (class)
- helps in data hiding and protecting the internal state of an object from outside interference
- In Python, encapsulation can be achieved by using private variables and methods, indicated by a leading double underscore (`__`).

## Inheritance
- Inheritance allows a class (subclass or derived class) to inherit properties and methods from another class (superclass or base class)
- It promotes code reusability and establishes a hierarchical relationship between classes.
- syntax: ```class DerivedClassName(BaseClassName):```

## Polymorphism
- the ability of objects to take on multiple forms or behaviors depending on their context.
- it allows us to use a single type, variable, or method for different types of actions.
- In Python, polymorphism is achieved through method overriding  and method overloading .

###  Types of polymorphism
1. **Method Overloading** - defining multiple methods with the same name but different parameters. aka compile time polymorphism
2. **Method Overriding** - redefining a method in the subclass with same name and parameters. aka run time polymorphism


# NOTE : 
- Python does not support method overloading(compile time polymorphism) in the traditional sense as seen in languages like Java or C++. In those languages, we can have multiple methods with the same name but different parameters, and the correct method is chosen based on the number or types of parameters passed.

- In Python, we can only have one method with a particular name in a class. If we define multiple methods with the same name, the last method definition will override the previous ones. Python does not consider the number or types of parameters when determining which method to call.

- However, we can achieve similar behavior by using default parameter values or variable-length arguments (*args, **kwargs) in Python. This allows a single method to handle different numbers or types of arguments.

Here's an example using default parameter values for achieving method "overloading" in Python:

```python
class Calculator:
    def add(self, a, b=0):
        return a + b

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.add(2))     # Output: 2
```
## Abstraction
