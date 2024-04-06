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
  